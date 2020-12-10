import model.vardict as mv

OPS = {
    'leq': lambda x,y:  x <= y,
    'geq': lambda x,y:  x >= y,
    'lt': lambda x,y:  x < y,
    'gt': lambda x,y:  x > y,
    'eq': lambda x,y:  x == y,
    'ne': lambda x,y:  x != y
}

class Rule:

    def __init__(self, p_dict, q_dict, ops, model):
        self.p = mv.VarDict(p_dict)
        self.q = mv.VarDict(q_dict)
        self.ops = {var_name:OPS[op_str] for var_name, op_str in ops.items()}
        self.model = model

    def trigger(self):
        """Intenta disparar la regla bajo el modelo actual y devuelve el resultado
        de su aplicabilidad."""
        result = self.p.match(self.model, self.ops)
        if result == mv.YES:
            self.q.apply(self.model)
        return result

    def lacking(self):
        """Devuelve un Set con las variables para las cuales falta informacion.
        Notar que tanto las ya aplicadas como algunas descartadas tienen lacking
        vacio, y las aplicables no."""
        return self.p.lacking(self.model)
