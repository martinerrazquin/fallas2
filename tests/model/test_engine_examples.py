import unittest

from model.engine import Engine


class KnownExamplesTest(unittest.TestCase):
    base_vars = ["mes", "sustentabilidad deseada", "ultimo cultivo", "regimen de lluvia", "capacidad de inversion",
                 "tipo de explotacion"]
    target_var = 'tipo de cultivo'
    rules = {
        "r1": {
            "given": {
                "sustentabilidad deseada": "alta"
            },
            "ops": {
                "sustentabilidad deseada": "eq"
            },
            "then": {
                "sustentabilidad requerida": 3
            }
        },
        "r2": {
            "given": {
                "sustentabilidad deseada": "baja"
            },
            "ops": {
                "sustentabilidad deseada": "eq"
            },
            "then": {
                "sustentabilidad requerida": 1
            }
        },
        "r3a": {
            "given": {
                "sustentabilidad deseada": "media",
                "ultimo cultivo": "soja"
            },
            "ops": {
                "sustentabilidad deseada": "eq",
                "ultimo cultivo": "eq"
            },
            "then": {
                "sustentabilidad requerida": 3
            }
        },
        "r3b": {
            "given": {
                "sustentabilidad deseada": "media",
                "ultimo cultivo": "girasol"
            },
            "ops": {
                "sustentabilidad deseada": "eq",
                "ultimo cultivo": "eq"
            },
            "then": {
                "sustentabilidad requerida": 3
            }
        },
        "r4a": {
            "given": {
                "sustentabilidad deseada": "media",
                "ultimo cultivo": "trigo"
            },
            "ops": {
                "sustentabilidad deseada": "eq",
                "ultimo cultivo": "eq"
            },
            "then": {
                "sustentabilidad requerida": 1
            }
        },
        "r4b": {
            "given": {
                "sustentabilidad deseada": "media",
                "ultimo cultivo": "sorgo"
            },
            "ops": {
                "sustentabilidad deseada": "eq",
                "ultimo cultivo": "eq"
            },
            "then": {
                "sustentabilidad requerida": 1
            }
        },
        "r4c": {
            "given": {
                "sustentabilidad deseada": "media",
                "ultimo cultivo": "maiz"
            },
            "ops": {
                "sustentabilidad deseada": "eq",
                "ultimo cultivo": "eq"
            },
            "then": {
                "sustentabilidad requerida": 1
            }
        },
        "r5a": {
            "given": {
                "sustentabilidad deseada": "media",
                "ultimo cultivo": "avena"
            },
            "ops": {
                "sustentabilidad deseada": "eq",
                "ultimo cultivo": "eq"
            },
            "then": {
                "sustentabilidad requerida": 2
            }
        },
        "r5b": {
            "given": {
                "sustentabilidad deseada": "media",
                "ultimo cultivo": "cebada"
            },
            "ops": {
                "sustentabilidad deseada": "eq",
                "ultimo cultivo": "eq"
            },
            "then": {
                "sustentabilidad requerida": 2
            }
        },
        "r6": {
            "given": {
                "regimen de lluvia": "bajo",
                "mes": 9
            },
            "ops": {
                "regimen de lluvia": "eq",
                "mes": "leq"
            },
            "then": {
                "resiliencia buscada": 3
            }
        },
        "r7a": {
            "given": {
                "regimen de lluvia": "bajo",
                "mes": 9
            },
            "ops": {
                "regimen de lluvia": "eq",
                "mes": "gt"
            },
            "then": {
                "resiliencia buscada": 2
            }
        },
        "r7b": {
            "given": {
                "regimen de lluvia": "alto",
                "mes": 9
            },
            "ops": {
                "regimen de lluvia": "eq",
                "mes": "leq"
            },
            "then": {
                "resiliencia buscada": 2
            }
        },
        "r7c": {
            "given": {
                "regimen de lluvia": "medio"
            },
            "ops": {
                "regimen de lluvia": "eq"
            },
            "then": {
                "resiliencia buscada": 2
            }
        },
        "r8": {
            "given": {
                "regimen de lluvia": "alto",
                "mes": 9
            },
            "ops": {
                "regimen de lluvia": "eq",
                "mes": "gt"
            },
            "then": {
                "resiliencia buscada": 1
            }
        },
        "r9a": {
            "given": {
                "capacidad de inversion": 1,
                "mes": 4,
                "resiliencia buscada": 1
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "leq",
                "resiliencia buscada": "leq"
            },
            "then": {
                "tipo de cultivo": "avena"
            }
        },
        "r9b": {
            "given": {
                "capacidad de inversion": 1,
                "mes": 4,
                "resiliencia buscada": 2
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "leq",
                "resiliencia buscada": "leq"
            },
            "then": {
                "tipo de cultivo": "avena"
            }
        },
        "r10": {
            "given": {
                "capacidad de inversion": 1,
                "mes": 4,
                "resiliencia buscada": 3
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "leq",
                "resiliencia buscada": "leq"
            },
            "then": {
                "tipo de cultivo": "cebada"
            }
        },
        "r11": {
            "given": {
                "capacidad de inversion": 1,
                "mes": 4
            },
            "ops": {
                "capacidad de inversion": "eq",
                "mes": "gt"
            },
            "then": {
                "tipo de cultivo": "sorgo"
            }
        },
        "r12aaa": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 2,
                "sustentabilidad requerida": 2,
                "tipo de explotacion": "agricola"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "trigo"
            }
        },
        "r12baa": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 3,
                "sustentabilidad requerida": 2,
                "tipo de explotacion": "agricola"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "trigo"
            }
        },
        "r12aba": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 2,
                "sustentabilidad requerida": 3,
                "tipo de explotacion": "agricola"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "trigo"
            }
        },
        "r12aab": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 2,
                "sustentabilidad requerida": 2,
                "tipo de explotacion": "mixta"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "trigo"
            }
        },
        "r12bba": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 3,
                "sustentabilidad requerida": 3,
                "tipo de explotacion": "agricola"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "trigo"
            }
        },
        "r12abb": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 2,
                "sustentabilidad requerida": 3,
                "tipo de explotacion": "mixta"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "trigo"
            }
        },
        "r12bab": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 3,
                "sustentabilidad requerida": 2,
                "tipo de explotacion": "mixta"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "trigo"
            }
        },
        "r12bbb": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 3,
                "sustentabilidad requerida": 3,
                "tipo de explotacion": "mixta"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "trigo"
            }
        },
        "r13a": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 2,
                "tipo de explotacion": "ganadera"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "avena"
            }
        },
        "r13b": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 3,
                "tipo de explotacion": "ganadera"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "avena"
            }
        },
        "r14aa": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 2,
                "sustentabilidad requerida": 1,
                "tipo de explotacion": "agricola"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "cebada"
            }
        },
        "r14ab": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 2,
                "sustentabilidad requerida": 1,
                "tipo de explotacion": "mixta"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "cebada"
            }
        },
        "r14ba": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 3,
                "sustentabilidad requerida": 1,
                "tipo de explotacion": "agricola"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "cebada"
            }
        },
        "r14bb": {
            "given": {
                "mes": 4,
                "capacidad de inversion": 3,
                "sustentabilidad requerida": 1,
                "tipo de explotacion": "mixta"
            },
            "ops": {
                "mes": "leq",
                "capacidad de inversion": "geq",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "cebada"
            }
        },
        "r15": {
            "given": {
                "capacidad de inversion": 2,
                "mes": 4,
                "tipo de explotacion": "ganadera"
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "gt",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "sorgo"
            }
        },
        "r16": {
            "given": {
                "capacidad de inversion": 2,
                "mes": 4,
                "tipo de explotacion": "agricola"
            },
            "ops": {
                "capacidad de inversion": "eq",
                "mes": "gt",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "girasol"
            }
        },
        "r17": {
            "given": {
                "capacidad de inversion": 2,
                "mes": 4,
                "tipo de explotacion": "mixta",
                "sustentabilidad requerida": 3,
                "resiliencia buscada": 1
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "gt",
                "tipo de explotacion": "eq",
                "sustentabilidad requerida": "leq",
                "resiliencia buscada": "leq"
            },
            "then": {
                "tipo de cultivo": "sorgo"
            }
        },
        "r18aa": {
            "given": {
                "capacidad de inversion": 2,
                "mes": 4,
                "tipo de explotacion": "mixta",
                "sustentabilidad requerida": 1
            },
            "ops": {
                "capacidad de inversion": "eq",
                "mes": "gt",
                "tipo de explotacion": "eq",
                "sustentabilidad requerida": "leq"
            },
            "then": {
                "tipo de cultivo": "girasol"
            }
        },
        "r18ba": {
            "given": {
                "capacidad de inversion": 2,
                "mes": 4,
                "tipo de explotacion": "mixta",
                "sustentabilidad requerida": 2
            },
            "ops": {
                "capacidad de inversion": "eq",
                "mes": "gt",
                "tipo de explotacion": "eq",
                "sustentabilidad requerida": "leq"
            },
            "then": {
                "tipo de cultivo": "girasol"
            }
        },
        "r18ab": {
            "given": {
                "capacidad de inversion": 2,
                "mes": 4,
                "tipo de explotacion": "mixta",
                "resiliencia buscada": 2
            },
            "ops": {
                "capacidad de inversion": "eq",
                "mes": "gt",
                "tipo de explotacion": "eq",
                "resiliencia buscada": "leq"
            },
            "then": {
                "tipo de cultivo": "girasol"
            }
        },
        "r18ab": {
            "given": {
                "capacidad de inversion": 2,
                "mes": 4,
                "tipo de explotacion": "mixta",
                "resiliencia buscada": 3
            },
            "ops": {
                "capacidad de inversion": "eq",
                "mes": "gt",
                "tipo de explotacion": "eq",
                "resiliencia buscada": "leq"
            },
            "then": {
                "tipo de cultivo": "girasol"
            }
        },
        "r19a": {
            "given": {
                "capacidad de inversion": 3,
                "mes": 4,
                "sustentabilidad requerida": 1,
                "tipo de explotacion": "agricola"
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "gt",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "soja"
            }
        },
        "r19b": {
            "given": {
                "capacidad de inversion": 3,
                "mes": 4,
                "sustentabilidad requerida": 1,
                "tipo de explotacion": "mixta"
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "gt",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "soja"
            }
        },
        "r20": {
            "given": {
                "capacidad de inversion": 3,
                "mes": 4,
                "sustentabilidad requerida": 3,
                "resiliencia buscada": 1
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "gt",
                "sustentabilidad requerida": "leq",
                "resiliencia buscada": "leq"
            },
            "then": {
                "tipo de cultivo": "maiz"
            }
        },
        "r21": {
            "given": {
                "capacidad de inversion": 3,
                "mes": 4,
                "tipo de explotacion": "ganadera",
                "resiliencia buscada": 1
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "gt",
                "tipo de explotacion": "eq",
                "resiliencia buscada": "leq"
            },
            "then": {
                "tipo de cultivo": "maiz"
            }
        },
        "r22": {
            "given": {
                "capacidad de inversion": 3,
                "mes": 4,
                "resiliencia buscada": 2,
                "tipo de explotacion": "ganadera"
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "gt",
                "resiliencia buscada": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "sorgo"
            }
        },
        "r23a": {
            "given": {
                "capacidad de inversion": 3,
                "mes": 4,
                "sustentabilidad requerida": 2,
                "tipo de explotacion": "agricola"
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "gt",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "girasol"
            }
        },
        "r23b": {
            "given": {
                "capacidad de inversion": 3,
                "mes": 4,
                "sustentabilidad requerida": 2,
                "tipo de explotacion": "mixta"
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "gt",
                "sustentabilidad requerida": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "girasol"
            }
        },
        "r24a": {
            "given": {
                "capacidad de inversion": 3,
                "mes": 4,
                "sustentabilidad requerida": 3,
                "resiliencia buscada": 2,
                "tipo de explotacion": "mixta"
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "gt",
                "sustentabilidad requerida": "leq",
                "resiliencia buscada": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "sorgo"
            }
        },
        "r24b": {
            "given": {
                "capacidad de inversion": 3,
                "mes": 4,
                "sustentabilidad requerida": 3,
                "resiliencia buscada": 2,
                "tipo de explotacion": "ganadera"
            },
            "ops": {
                "capacidad de inversion": "geq",
                "mes": "gt",
                "sustentabilidad requerida": "leq",
                "resiliencia buscada": "leq",
                "tipo de explotacion": "eq"
            },
            "then": {
                "tipo de cultivo": "sorgo"
            }
        }
    }

    def test_soja(self):
        e = Engine(self.base_vars, self.target_var)
        for rule in self.rules.values():
            e.add_rule(rule["given"], rule["then"], rule["ops"])

        e.step('sustentabilidad deseada', "baja")
        e.step('regimen de lluvia', "bajo")
        e.step('mes', 10)
        e.step('capacidad de inversion', 3)
        e.step('tipo de explotacion', "agricola")

        self.assertEqual("soja", e.recommend())

    def test_girasol(self):
        e = Engine(self.base_vars, self.target_var)
        for rule in self.rules.values():
            e.add_rule(rule["given"], rule["then"], rule["ops"])

        e.step('sustentabilidad deseada', "baja")
        e.step('regimen de lluvia', "bajo")
        e.step('mes', 10)
        e.step('capacidad de inversion', 2)
        e.step('tipo de explotacion', "agricola")

        self.assertEqual("girasol", e.recommend())

    def test_sorgo(self):
        e = Engine(self.base_vars, self.target_var)
        for rule in self.rules.values():
            e.add_rule(rule["given"], rule["then"], rule["ops"])

        e.step('sustentabilidad deseada', "baja")
        e.step('regimen de lluvia', "bajo")
        e.step('mes', 10)
        e.step('capacidad de inversion', 2)
        e.step('tipo de explotacion', "ganadera")

        self.assertEqual("sorgo", e.recommend())

    def test_sorgo_mixed_questions(self):
        e = Engine(self.base_vars, self.target_var)
        for rule in self.rules.values():
            e.add_rule(rule["given"], rule["then"], rule["ops"])

        e.step('sustentabilidad deseada', "alta")
        e.step('regimen de lluvia', "medio")
        e.step('mes', 11)
        e.step('capacidad de inversion', 3)
        e.step('tipo de explotacion', "mixta")

        self.assertEqual("sorgo", e.recommend())

    def test_maiz(self):
        e = Engine(self.base_vars, self.target_var)
        for rule in self.rules.values():
            e.add_rule(rule["given"], rule["then"], rule["ops"])

        e.step('sustentabilidad deseada', "alta")
        e.step('regimen de lluvia', "alto")
        e.step('mes', 11)
        e.step('capacidad de inversion', 3)
        e.step('tipo de explotacion', "mixta")

        self.assertEqual("maiz", e.recommend())

    def test_cebada(self):
        e = Engine(self.base_vars, self.target_var)
        for rule in self.rules.values():
            e.add_rule(rule["given"], rule["then"], rule["ops"])

        e.step('sustentabilidad deseada', "media")
        e.step('regimen de lluvia', "bajo")
        e.step('mes', 3)
        e.step('capacidad de inversion', 2)
        e.step('ultimo cultivo', "media")

        self.assertEqual("cebada", e.recommend())