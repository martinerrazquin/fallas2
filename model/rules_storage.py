import json

RULES_PATH = "./resources/rules.json"


def read(path):
    with open(path) as json_rules:
        try:
            return json.load(json_rules)
        except:
            return {}
