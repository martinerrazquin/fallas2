import unittest
from model.rules_storage import read, RULES_PATH


class ReadingRulesTest(unittest.TestCase):
    expected_rules = {
        "rule1": {
            "given": {
                "b": 2,
                "c": 3
            },
            "then": {
                "y": 4
            }
        },
        "rule2": {
            "given": {
                "y": 4,
                "a": 1
            },
            "then": {
                "x": "hola"
            }
        },
        "rule3": {
            "given": {
                "a": -1,
                "b": -1,
                "c": -1
            },
            "then": {
                "y": -1
            }
        },
        "rule4": {
            "given": {
                "y": -1
            },
            "then": {
                "x": "chau"
            }
        }
    }

    def test_readEmptyFile_thenReturnEmptySet(self):
        rules = read("../resources/empty_rules.json")

        self.assertFalse(bool(rules))

    def test_readRules(self):
        rules = read("../resources/rules.json")

        self.assertEqual(4, len(rules["rules"]))

        self.assertEqual(self.expected_rules, rules["rules"])

    def test_readBaseVars(self):
        rules = read("../resources/rules.json")

        self.assertEqual(["a", "b", "c"], rules["base_vars"])

    def test_readTargetVars(self):
        rules = read("../resources/rules.json")

        self.assertEqual(["x"], rules["target_vars"])


if __name__ == '__main__':
    unittest.main()
