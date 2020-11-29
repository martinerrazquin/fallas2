import unittest

from model.engine import Engine


class OneBaseOneTargetEngineTest(unittest.TestCase):

    def test_oneRule_baseDoesNotMatch_thenTargetDoesNotMatch(self):
        e = Engine(['a'], 'm')
        e.add_rule({'a': 1}, {'m': 1})
        e.step('a', 0)
        self.assertFalse(e.does_rule_matches('m'))

    def test_oneRule_baseMatches_thenTargetMatches(self):
        e = Engine(['a'], 'm')
        e.add_rule({'a': 1}, {'m': 1})
        e.step('a', 1)
        self.assertTrue(e.does_rule_matches('m'))

    def test_oneRule_baseCannotBeAddedTwice(self):
        e = Engine(['a'], 'm')
        e.add_rule({'a': 1}, {'m': 1})
        e.step('a', 1)
        with self.assertRaises(KeyError):
            e.step('a', 0)

    def test_twoRules_rulesWithSameBase_thenFormLogicOR(self):
        e = Engine(['a'], 'm')
        e.add_rule({'a': 1}, {'m': 1})
        e.add_rule({'a': 0}, {'m': 1})

        e.step('a', 0)
        self.assertTrue(e.does_rule_matches('m'))

        e = Engine(['a'], 'm')
        e.add_rule({'a': 1}, {'m': 1})
        e.add_rule({'a': 0}, {'m': 1})

        e.step('a', 1)
        self.assertTrue(e.does_rule_matches('m'))

    def test_twoRules_noContradictionAllowed(self):
        e = Engine(['a'], 'm')
        e.add_rule({'a': 1}, {'m': 1})
        with self.assertRaises(ValueError):
            e.add_rule({'a': 1}, {'m': 0})

if __name__ == '__main__':
    unittest.main()
