import json

RULES_PATH = "./resources/rules.json"


def __dict2list(rules_dict):
    parsed_rules = []

    for rule in rules_dict["rules"].values():
        parsed_rules.append((rule["given"], rule["then"], rule["ops"]))

    rules_dict["rules"] = parsed_rules
    return rules_dict


def read(path):
    with open(path) as json_rules:
        try:
            return __dict2list(json.load(json_rules))
        except:
            return {}
