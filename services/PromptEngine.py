class PromptEngine:
    def __init__(self):
        self.__prompts = {
            "plan_parser": lambda diet_plan: f'extract the food items and their time (in 24 hours format) as a json '
                                             f'object from the given'
                                             f'diet plan: {diet_plan}'
        }

    def get_prompt(self, prompt_type, file):
        return self.__prompts[prompt_type](file)