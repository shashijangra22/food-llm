import json

import yaml
from llamaapi import LlamaAPI


def transform_response(response):
    if response.status_code != 200:
        return []
    content = response.json()["choices"][0]["message"]["content"].split('```')[1].strip()
    return json.dumps(json.loads(content), indent=4)


class LLM:
    def __init__(self):
        self.__config = None
        self.__llm = None
        self.__model = "llama3-70b"
        self.__bootstrap()

    def get_filtered_results(self, plan, key_items, results):
        if self.__llm is None:
            return json.dumps(results, indent=4)
        req = self.__get_restaurant_request(key_items, results)
        try:
            response = self.__llm.run(req)
            print("Model response is: {}".format(response.json()))
            return transform_response(response)
        except Exception as e:
            print("Failed to get model response: ", e)
            return json.dumps(results, indent=4)

    def __get_restaurant_request(self, key_items, results):
        return {
            "model": self.__model,
            "messages": [
                {"role": "system",
                 "content": f"Given the restaurants with food items: {results}, filter the "
                            f"restaurants and their food items matching the user's diet items and return the response "
                            f"in json format"},
                {"role": "user",
                 "content": f"Based on the following diet items: {','.join(key_items)}, recommend me restaurants and "
                            f"food items and rank them by ratings, distance and relevance"},
            ]
        }

    def __bootstrap(self):
        try:
            with open("config/config.yaml", "r") as yaml_file:
                self.__config = yaml.safe_load(yaml_file)['LLMCONFIG']
                if self.__config['ENABLED'] and self.__config['API_KEY']:
                    self.__llm = LlamaAPI(self.__config['API_KEY'])
                    print("LLama is ready!")
                else:
                    print("LLama is not ready!")
        except Exception as e:
            print(e)
