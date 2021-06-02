# TP Fallas 2
Sistema experto para selección de cultivos, con motor de inferencia propio

## Backend
Para actualizar las librerias:

```
pipenv install
```

Para levantar el server:

```
pipenv run app
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

Una *regla* es una proposición de la forma *p -> q* donde *p, q* son *VarDict*'s,
más una lista de operaciones para comparar los valores de *p* contra el contexto.


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


## Ejemplos

### Ejemplo 1: soja

1. sustentabilidad deseada: baja
2. regimen de lluvia: bajo
3. mes: 10 (octubre)
4. capacidad de inversion: alta
5. tipo de explotacion: agricola

Sugiere soja

### Ejemplo 2: girasol
Si en el ejemplo anterior se cambia la capacidad de inversion a media, cambia
el resultado:

1. sustentabilidad deseada: baja
2. regimen de lluvia: bajo
3. mes: 10 (octubre)
4. *capacidad de inversion: media*
5. tipo de explotacion: agricola

Sugiere girasol

### Ejemplo 3: sorgo
Si ahora se cambia el tipo de explotación a ganadera, el girasol pierde relevancia,
y se sugiere sorgo en su lugar.

1. sustentabilidad deseada: baja
2. regimen de lluvia: bajo
3. mes: 10 (octubre)
4. capacidad de inversion: media
5. *tipo de explotacion: ganadera*

Sugiere sorgo

### Ejemplo 4: sorgo
En este ejemplo se puede ver cómo cambian de orden las preguntas al cobrar más
relevancia otras:

1. sustentabilidad deseada: alta
2. regimen de lluvia: medio *(este valor y el anterior cambian el orden de las dos siguientes)*
3. capacidad de inversion: alta *(ahora pregunta por esto antes que el mes)*
4. mes: 11 (noviembre)
5. tipo de explotacion: mixta

Sugiere sorgo

### Ejemplo 5: maíz
Si sobre el ejemplo anterior se provee un regimen de lluvia alto, se vuelve viable
sembrar maiz

1. sustentabilidad deseada: alta
2. *regimen de lluvia: alto*
3. capacidad de inversion: alta
4. mes: 11 (noviembre)
5. tipo de explotacion: mixta

Sugiere maíz

### Ejemplo 6: cebada
Ante cierto valor pueden aparecer otras preguntas:

1. *sustentabilidad deseada: media*
2. ultimo cultivo: soja    *(esta pregunta aparece por el valor de la anterior)*
3. regimen de lluvia: bajo
4. mes: 3 (marzo)
3. capacidad de inversion: media

Sugiere cebada
