YES = 1
NO = -1
UNKNOWN = 0

class VarDict:

    def __init__(self,name_value_mapping):
        self.d = name_value_mapping

    def match(self,context):
        """Compara contra el contexto (base de conocimientos) brindado y devuelve
        alguna una de las constantes de clase:
        YES, si todos los mapeos coinciden
        NO, si algun mapeo no coincide
        UNKNOWN, si algun mapeo no existe pero los existentes coinciden (faltan datos)."""

        all_mappings_exist = YES
        for var_name, expected_value in self.d.items():
            true_value = context.get(var_name,None)
            if true_value is None:
                all_mappings_exist = UNKNOWN
            elif true_value != expected_value:
                return NO

        return all_mappings_exist

    def apply(self,context):
        """Aplica su mapeo al contexto. Si alguna variable ya existia con un
        valor distinto, arroja ValueError."""

        for var_name, expected_value in self.d.items():
            # si esta definida, devuelve el valor actual, sino aplica y devuelve expected_value
            context_value = context.setdefault(var_name, expected_value)
            if context_value != expected_value:
                raise ValueError('{}: expected {} and got {}'.format(var_name,
                    expected_value, context_value))

    def lacking(self,context):
        """Devuelve un Set con las keys que maneja el VarDict que no se encuentran en el
        contexto"""
        got = {k for k in self.d.keys()}
        found = {k for k in context.keys()}
        return got - found
