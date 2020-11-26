# TP Fallas 2
Sistema experto para selección de cultivos, con motor de inferencia propio

## *TODO*

* pruebas sobre el motor (revisar que ande bien): sobre esto solo hay un poco de
codigo en engine.py
* agregar un parser de json/yaml para levantar los valores posibles, preguntas, reglas, etc.
* agregar resources para el server de Flask
    * con un POST@/data, POST@/reset y GET@/recommend deberia estar bien
* agregar un frontend para las preguntas y eso


## Backend
Para actualizar las librerias:

```
pipenv install
```

Para levantar el server:

```
pipenv run start
```

## Modelo

### VarDict

Un *VarDict* es un diccionario con mapeos de la forma *var\_name -> var\_value*
y se usa para describir un contexto, sea:

* El requerido para disparar una regla
* El conocimiento que aporta una regla al dispararse
* La base de conocimientos actual

Si un *VarDict* aplica, se considera que todas sus variables toman los valores
que especifica.

### Regla

Una *regla* es una proposición de la forma *p -> q* donde *p, q* son *VarDict*'s.


### Motor

El motor se define con:

* Una lista de variables *base*: aquellas que puede ingresar el usuario.
* Una variable *target*: aquella cuyo valor se desea conocer.

Para el mismo se definen las siguientes acciones:

* *agregar una regla*
* *recomendar un valor* para la variable *target*
* *obtener la mejor variable base faltante*
* *realizar un paso de inferencia* donde se agrega un valor a una variable base faltante y
se aplica *forward propagation* a las reglas.


Un esquema de trabajo es:

1. Definir el motor, agregar las reglas
2. Mientras se pueda obtener una mejor variable base faltante *x*:
    1. el usuario ingresa el valor de *x*, se realiza un paso de inferencia
    2. si se encontró un valor para la variable target, se corta el ciclo
3. se da una recomendación para la variable target, siendo una conclusión fuerte
si se encontró un valor para la misma en el modelo o una aproximación si no
