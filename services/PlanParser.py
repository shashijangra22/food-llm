from collections import defaultdict


class PlanParser:
    def __init__(self):
        pass
        # integrate LLM here to parse the input plan

    def parse_plan(self, input_plan):
        line_items = input_plan.strip().split("\n")
        plan = defaultdict(list)
        for item in line_items:
            tokens = item.split(',')
            time = ":".join(x.zfill(2) for x in tokens[0].strip().split(':'))
            food_items = []
            for food_item in tokens[1:]:
                ind = food_item.index('(')
                name = food_item[:ind].strip()
                qty = food_item[ind:].strip()[1:-1]
                food_items.append({'name': name, 'qty': qty})
            plan[time] = food_items
        return plan
