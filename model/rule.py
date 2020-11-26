import vardict as mv

class Rule:

    def __init__(self,p_dict,q_dict,model):
        self.p = mv.VarDict(p_dict)
        self.q = mv.VarDict(q_dict)
        self.model = model

    def trigger(self):
        """Intenta disparar la regla bajo el modelo actual y devuelve el resultado
        de su aplicabilidad."""
        result = self.p.match(self.model)
        if result == mv.YES:
            self.q.apply(self.model)
        return result

    def lacking(self):
        """Devuelve un Set con las variables para las cuales falta informacion.
        Notar que tanto las ya aplicadas como algunas descartadas tienen lacking
        vacio, y las aplicables no."""
        return self.p.lacking(self.model)
