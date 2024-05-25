import json
from collections import defaultdict


def matches(rest_item, diet_items):
    # print(f"matching {rest_item} with {diet_items}")
    diet_item_tokens = [token.lower() for item in diet_items for token in item.split()]
    rest_item_tokens = [token.lower() for token in rest_item.split()]
    for token in rest_item_tokens:
        if token in diet_item_tokens:
            return True
    return False


class RestaurantService:
    def __init__(self):
        self.__restaurants = defaultdict()
        self.__bootstrap()

    def get_restaurants(self, items, loc):
        restaurants = []
        for rest in self.__restaurants[loc.lower()]:
            for food_item in rest["food_items"]:
                if matches(food_item["item"], items):
                    restaurants.append(rest)
                    break
        return restaurants

    def __bootstrap(self):
        try:
            with open("storage/restaurants.json", "r") as f:
                result = defaultdict(list)
                for res in json.loads(f.read()):
                    result[res["city"].lower()].append(res)
                self.__restaurants = result
        except Exception as e:
            print(e)
