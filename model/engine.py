import model.rule as mr, model.vardict as mv


class Engine:
    def __init__(self, base_vars, target_var):
        self.applicable_rules = []
        self.discarded_rules = []
        self.applied_rules = []
        self.target_var = target_var
        self.base_vars = set(base_vars)
        self.model = {}

    def add_rule(self, p_dict, q_dict, ops={}):
        # TODO: agregar un Dict: var_name -> Set() de posibles valores para cada mapeo?
        # contradictions = any(filter(lambda rule: (rule.p.to_dict() == p_dict) and (rule.q != q_dict), self.applicable_rules))
        # if contradictions:
        #     raise ValueError("Contradicting rules provided")

        self.applicable_rules.append(mr.Rule(p_dict, q_dict, ops, self.model))

    def step(self, new_var_name, new_var_value):
        if new_var_name in self.model:
            raise KeyError("{} already exists in model".format(new_var_name))
        self.model[new_var_name] = new_var_value

        while not (t := self.target_var in self.model):
            new_applicable = []

            for rule in self.applicable_rules:
                print(rule.p.d, "->", rule.q.d)
                result = rule.trigger()
                # si no se puede hacer nada, preparar para reencolar
                if result == mv.UNKNOWN:
                    new_applicable.append(rule)
                elif result == mv.YES:
                    self.applied_rules.append(rule)
                elif result == mv.NO:
                    self.discarded_rules.append(rule)
            # si no se aplico ni descarto nada, no hace falta seguir iterando...
            if len(new_applicable) == len(self.applicable_rules):
                break
            # ...sino, actualizar las aplicables y volver a probar
            self.applicable_rules = new_applicable

        return t

    def get_next_var(self):
        # solo considero aquellas reglas que se completan con variables base
        weighted_list = [(rule, rule.lacking()) for rule in self.applicable_rules
                         if rule.lacking() <= self.base_vars]
        print(weighted_list)
        if len(weighted_list) == 0:
            return None  # raise ValueError("Model can't be further extended")
        winning_rule, lacking_vars = sorted(weighted_list, key=lambda x: len(x[1]))[0]
        # devolver la primer variable base que falte
        return lacking_vars.pop()

    def recommend(self):
        # TODO: agregar una recomendacion cuando target_var no esta definida
        return self.model[self.target_var]

    def reset(self):
        # reset rules
        self.applicable_rules = self.applicable_rules + self.applied_rules + self.discarded_rules
        self.discarded_rules = []
        self.applied_rules = []

        # reset model
        self.model = {}

        # reset rules' model
        for rule in self.applicable_rules:
            rule.model = self.model

    def get_model(self):
        return self.model

    def does_rule_matches(self, param):
        return param in self.get_model()


# testing
if __name__ == '__main__':
    def f(x, y):
        print(e.step(x, y))
        print('Proximo:', e.get_next_var())
        print('disp:', len(e.applicable_rules), ', ok:', len(e.applied_rules),
              ', no:', len(e.discarded_rules))


    e = Engine(['a', 'b', 'c', 'd'], 'm')
    e.add_rule({'a': 1, 'b': 2}, {'u': 3}, {'a':'eq','b':'eq'})
    e.add_rule({'a': 1, 'u': 2}, {'v': 7}, {'a': 'eq', 'u': 'eq'})
    e.add_rule({'a': 1, 'u': 3, 'c': 3}, {'v': 9},{'a': 'eq', 'u': 'eq', 'c': 'eq'})
    e.add_rule({'a': 1, 'd': 4}, {'w': 10},{'a': 'eq', 'd': 'eq'})
    e.add_rule({'v': 9, 'w': 10}, {'m': 999},{'v': 'eq', 'w': 'eq'})
    e.add_rule({'v': 9, 'y': 16}, {'m': 0},{'v': 'eq', 'y': 'eq'})
    f('a', 1)
    f('b', 2)
    f('c', 3)
    # f('d',1)
    f('d', 4)
    print('------------------')
    if 'm' not in e.model:
        print("no hay solucion")
    else:
        print("solucion:", e.model['m'])
