import json
from bisect import bisect_left

from models import Errors
from services.LLM import LLM
from services.PlanParser import PlanParser
from services.RestaurantService import RestaurantService


def get_key_items(plan, req):
    times = list(plan.keys())
    ind = bisect_left(times, req.time)
    if ind >= len(times):
        return []
    return [meal["name"] for meal in plan[times[ind]]]


class Foody:
    def __init__(self):
        self.__plan_parser = PlanParser()
        self.__restaurant_service = RestaurantService()
        self.__llm = LLM()

    def get_recommendations(self, req):
        plan = self.__plan_parser.parse_plan(req.plan)
        key_items = get_key_items(plan, req)
        if len(key_items) == 0:
            return [], Errors.ERROR_LATE_TIMING
        res = self.__restaurant_service.get_restaurants(key_items, req.loc)
        if len(res) == 0:
            return [], Errors.ERROR_NO_RESTAURANTS
        results = self.__llm.get_filtered_results(req.plan, key_items, res)
        return results, None
