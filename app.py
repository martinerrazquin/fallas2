from flask import Flask
from flask_cors import CORS, cross_origin

import model.engine as me
from model.rules_storage import read
from os.path import join, dirname, realpath
app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': '*'}})

def present_next_var():
    nv = eng.get_next_var()
    if nv is None:
        return None
    pv = possible_values[nv]
    q = questions[nv]
    return {'name': nv, 'question': q, 'possible values': pv}


@app.route('/')
def hello():
    return {'disp': len(eng.applicable_rules), 'applied': len(eng.applied_rules),
            'discarded': len(eng.discarded_rules)}


@app.route('/reset', methods=['GET'])
def reset():
    eng.reset()
    return {'next_var': present_next_var()}


# FIXME: que sea un POST @/data y se parsea usando el tipo de variable definido en Loader
@app.route('/data/<var>/<value>', methods=['GET'])
def data(var, value):
    try:
        value = int(value)
    except ValueError:
        pass
    if (conv := eng.step(var, value)):
        return {'convergence': conv, 'next_var': None}
    return {'convergence': conv, 'next_var': present_next_var()}


@app.route('/recommend', methods=['GET'])
def recommend():
    return {'recommendation': eng.recommend()}


@app.route('/debug/state', methods=['GET'])
def state():
    return {k: v for k, v in eng.model.items()}


def _setup():
    # FIXME: hardcoded, parse the real stuff from json/yaml
    base_vars = ['mes', 'inv', 'lluvia']
    target_var = 'x'
    parsed_rules = [({'mes': 4, 'inv': "alto"}, {'x': "soja"}, {'mes': "gt", 'inv': "eq"}),
                    ({'mes': 4, 'lluvia': 3}, {'rb': 'si'}, {'mes': "gt", 'lluvia': "leq"}),
                    ({'mes': 4}, {'rb': 'si'}, {'mes': "leq"}),
                    ({'rb': "si", 'inv': "bajo"}, {'x': "pasto"}, {'rb': "eq", 'inv': "eq"})]
    questions = {'mes': 'preg1', 'inv': 'preg2', 'lluvia': 'preg3'}
    possible_values = {'mes': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
                       'inv': ['bajo', 'medio', 'alto'],
                       'lluvia': [1, 2, 3]}
    # init engine

    rules = read(join(dirname(realpath(__file__)), "./resources/rules_posta.json"))

    base_vars = rules["base_vars"]
    target_var = rules["target_var"]
    parsed_rules = rules["rules"]
    questions = rules["questions"]
    possible_values = rules["possible_values"]
    eng = me.Engine(base_vars, target_var)
    for p, q, ops in parsed_rules:
        eng.add_rule(p, q, ops)
    return eng, questions, possible_values

eng, questions, possible_values = _setup()
if __name__ == '__main__':

    app.run(debug=True, port=5000)
