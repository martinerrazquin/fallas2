from flask import Flask
from flask_cors import CORS, cross_origin

import model.engine as me

app = Flask(__name__)
cors = CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/')
def hello():
    return {'disp':len(eng.applicable_rules), 'applied':len(eng.applied_rules),
            'discarded':len(eng.discarded_rules)}

@app.route('/reset',methods=['GET'])
def reset():
    eng.reset()
    return {'next_var': eng.get_next_var()}

# FIXME: que sea un POST @/data y se parsea usando el tipo de variable definido en Loader
@app.route('/data/<var>/<value>',methods=['GET'])
def data(var,value):
    value = int(value)
    return {'convergence': eng.step(var,value), 'next_var': eng.get_next_var()}

@app.route('/recommend',methods=['GET'])
def recommend():
    return {'recommendation': eng.recommend()}

@app.route('/debug/state',methods=['GET'])
def state():
    return {k:v for k,v in eng.model.items()}

def _setup():
    # FIXME: hardcoded, parse the real stuff from json/yaml
    base_vars = ['a','b','c']
    target_var = 'x'
    parsed_rules = [({'b':2,'c':3},{'y':4}),({'y':4,'a':1},{'x':'hola'}),
                    ({'a':-1,'b':-1,'c':-1},{'y':-1}),({'y':-1},{'x':'chau'})]

    # init engine
    eng = me.Engine(base_vars,target_var)
    for p,q in parsed_rules:
        eng.add_rule(p,q)
    return eng

if __name__=='__main__':
    eng = _setup()
    app.run(debug=True, port=5000)
