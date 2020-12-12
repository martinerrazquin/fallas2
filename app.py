from flask import Flask
from flask_cors import CORS, cross_origin

import model.engine as me

app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': '*'}})

def _setup():
    # FIXME: hardcoded, parse the real stuff from json/yaml
    base_vars = ['mes', 'inv', 'lluvia']
    target_var = 'x'
    parsed_rules = [({'mes': 4, 'inv': "alto"}, {'x': "soja"},{'mes': "gt", 'inv': "eq"}),
                    ({'mes': 4, 'lluvia': 3}, {'rb': 'si'},{'mes': "gt", 'lluvia': "leq"}),
                    ({'mes': 4}, {'rb': 'si'},{'mes': "leq"}),
                    ({'rb': "si",'inv':"bajo"}, {'x': "pasto"},{'rb': "eq",'inv':"eq"})]
    questions = {'mes':'preg1','inv':'preg2','lluvia':'preg3'}
    possible_values = {'mes':[1,2,3,4,5,6,7,8,9,10,11,12],
                        'inv':['bajo','medio','alto'],
                        'lluvia':[1,2,3]}
    # init engine
    eng = me.Engine(base_vars, target_var)
    for p, q, ops in parsed_rules:
        eng.add_rule(p, q, ops)
    return eng,questions,possible_values

eng, questions, possible_values = _setup()

def present_next_var():
    nv = eng.get_next_var()
    pv = possible_values[nv]
    q = questions[nv]
    return {'name':nv,'question':q,'possible values':pv}

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
    return {'convergence': eng.step(var, value), 'next_var': present_next_var()}


@app.route('/recommend', methods=['GET'])
def recommend():
    return {'recommendation': eng.recommend()}


@app.route('/debug/state', methods=['GET'])
def state():
    return {k: v for k, v in eng.model.items()}




if __name__ == '__main__':
    app.run(debug=True, port=5000)
