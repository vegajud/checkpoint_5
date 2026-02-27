# Checkpoint 5

## ¿Qué es un condicional?
Los condicionales se utilizan para ejecutar ciertos bloques de código según condiciones específicas. Estas sentencias ayudan a controlar el flujo de un programa, haciendo que se comporte de forma diferente en distintas situaciones.
<br>
Los forman los siguientes elementos:

**- If**
<br>
Es la forma más simple de un condicional. Ejecuta un bloque de código si la condición dada es verdadera.

Ejemplo:
```
age = 25
if age >= 16:
    print("Puedes comprar en la página")
```

*Resultado:*
```
Puedes comprar en la página
```

**- If + Else**
<br>
Permite especificar un bloque de código que se ejecutará si la o las condiciones asociadas a una sentencia if (o elif) se evalúan como falsas. El bloque else permite gestionar todos los demás casos que no cumplen las condiciones especificadas.

*Ejemplo:*
```
height = 1.10
if height <= 1.50:
    print("El menú es gratis.")
else:
    print("Debes pagar el menú.")
```

*Resultado:*
```
El menú es gratis.
```

**- Elif**
<br>
Es la unión de "else if", que permite comprobar múltiples condiciones para ejecutar diferentes bloques de código según cuál sea verdadera. El uso de elif hace que nuestro código sea más legible y eficiente porque evita la necesidad de demasiadas sentencias if anidadas.

*Ejemplo:*
```
age = 28

if age <= 12:
    print("Eres un niño. Entras gratis.")
elif age <= 19:
    print("Eres un adolescente. Tienes descuento.")
elif age <= 59:
    print("Eres adulto. No tienes descuento.")
else:
    print("Eres anciano. Tienes descuento.")
```

*Resultado:*
```
Eres adulto. No tienes descuento.
```

**Condicionales ternarios**
<br>
Es una forma compacta de escribir una condición if-else en una sola línea. A veces se denomina "expresión condicional".

*Ejemplo:*
```
age = 10
payment = "Precio normal" if age >= 12 else "Gratuito"
print(payment)
```

*Resultado:*
```
Gratuito
```

## ¿Cuáles son los diferentes tipos de bucles en Python? ¿Por qué son útiles?
Los principales tipos de loops son los *For loops* y *While loops*. *For* resulta útil cuando se quiere realizar un loop en un rango concreto, por ejemplo si se quiere imprimir una secuencia de números y detenerse en uno específico. 
<br>
Sin embargo, cuando no se conoce el rango o el número de veces que se va a realizar el bucle, es más útil *While*. Sería el caso de los intentos de acceso a una cuenta de usuario, donde se puede introducir la contraseña de manera correcta o incorrecta. En el caso de que sea incorrecta, se necesitará ofrecer la opción de volver a intentarlo hasta introducir la correcta.

**- For**
<br>
Itera sobre una secuencia, que puede ser una lista, una tupla, una cadena/string o un rango. Ejecuta un bloque de código repetidamente, una vez por cada elemento de la secuencia/rango.

*Ejemplo:*
```
for num in range(1,6):
  print("num =", num)

print("Completado")
```

*Resultado:*
```
num = 1
num = 2
num = 3
num = 4
num = 5
Completado
```

En el ejemplo, se forma un loop siguiendo el rango indicado, del 1 al 5 (*range* excluye el límite superior, en este caso el *num = 6*). En ese momento imprimirá "Completado".

**- While**
<br>
Se utiliza para ejecutar un bloque de sentencias repetidamente hasta que se cumple una condición dada. Cuando la condición se vuelve falsa, se ejecuta la línea inmediatamente posterior al bucle en el programa.

*Ejemplo:*
```
contraseña = ''

while contraseña != 'IlovePython':
    contraseña = input('Introduce tu contraseña: ')

print('¡Bienvenido!')
```
En este ejemplo, mientras se introduzca una contraseña incorrecta seguirá el bucle, dando la opción de introducir un nuevo texto hasta que se escriba *"IlovePython"*. Cuando eso ocurra, el bucle finalizará y se imprimirá *"¡Bienvenido!"*. 

*Resultado:*
```
Introduce tu contraseña: dtjkhgldjrhd
Introduce tu contraseña: IlovePython
¡Bienvenido!
```
Se puede mejorar utilizando *while True*, que permite introducir la variable *"contraseña"* en el loop en vez de dejarla fuera como en el ejemplo anterior. 

```
while True:
    contraseña = input('Introduce tu contraseña: ')

    if contraseña == 'IlovePython':
      break

print('¡Bienvenido!')
```

*Resultado:*
```
Introduce tu contraseña: sjdfbgksjdbgjksfdh
Introduce tu contraseña: IlovePython
¡Bienvenido!
```

## ¿Qué es una lista por comprensión en Python?

Estas listas permiten una sintaxis más corta cuando desea crear una nueva lista basada en los valores de una ya existente. 

*Ejemplo:*

Sin usar una lista por comprensión la sintaxis sería la siguiente:

```
hobbies = ["libros", "videojuegos", "viajes", "dibujos"]
hobbies_reducidos = []

for hobby in hobbies:
  if "o" in hobby:
    hobbies_reducidos.append(hobby)

print(hobbies_reducidos)
```

*Resultado:*
```
['libros', 'videojuegos', 'dibujos']
```

Por lo tanto, la forma de realizarlo mediante listas por comprensión sería la siguiente:

```
hobbies = ["libros", "videojuegos", "viajes", "dibujos"]

hobbies_reducidos = [hobby for hobby in hobbies if "o" in hobby]

print(hobbies_reducidos)
```
El desglose de elementos para entenderla sería:

```
[hobby for hobby in hobbies if "o" in hobby]
```
Parte 1: operación/transformación. En este caso sólo es necesario utilizar *"hobby"* porque se van a seleccionar las variables que cumplan una condición, pero no se van a transformar.
<br>
Parte 2: *for* + variable (*hobby* en el ejemplo) + *in*.
<br>
Parte 3: lista original (*hobbies*).
<br>
Parte 4: se añade la condición *if*, que indica que la nueva lista sólo imprimirá los hobbies que contengan una *"o"*.

*Resultado:*
```
['libros', 'videojuegos', 'dibujos']
```

## ¿Qué es un argumento en Python?
Es lo que permite pasar información a las funciones.
<br>
Los argumentos se especifican después del nombre de la función, entre paréntesis, pudiendo agregar tantos argumentos como sean necesarios, simplemente separándolos con una coma.

*Ejemplo:*
```
def petición(argumento = 'algo'):
  print(f'Necesito {argumento}!')

petición()
petición('ayuda')
```
En el ejemplo se ha registrado *'algo'* por defecto/default, de modo que el código funcionará aunque no se registre un argumento concreto.

*Resultado:*
```
Necesito algo!
Necesito ayuda!
```
También es importante saber que por defecto, una función debe llamarse con el número correcto de argumentos, por lo que si una función espera dos argumentos, debe llamarse con exactamente dos argumentos.

*Ejemplo:*
```
def nombre_completo(nombre, apellido):
  print(nombre + " " + apellido)

nombre_completo("John", "Doe")
```
*Resultado:*
```
John Doe
```
Además, si queremos podemos darle un valor a la clave/key, de modo que el orden en el que se den los argumentos no sea importante (ya se ha indicado un orden).

*Ejemplo:*
```
def my_function(bebida, aditivo):
  print("Quiero", bebida)
  print("Quiero", bebida + " con", aditivo)

my_function(bebida = "café", aditivo = "leche")
```
*Resultado:*
```
Quiero café
Quiero café con leche
```

Existen diferentes tipos de argumentos utilizados para diferentes situaciones:

**- Arbitrary Arguments o Argumentos arbitrarios**
<br>
También llamados **args*, se utilizan si no conocemos cuántos argumentos de palabra clave se pasarán a la función, o para evitar utilizar un argumento diferente por cada añadido.

Utilizándolos la función recibe una tupla de argumentos a los que podrá acceder según corresponda.

*Ejemplo:*
```
def pedido(nom_cliente, tipo_bebida, *args):
  print(nom_cliente, "ha pedido", tipo_bebida)
  for arg in args:
    print("- Con", arg)

  
pedido("Jon", "cerveza")
pedido("Sara", "Coca-cola", "hielo", "limón")
```
*Resultado:*
```
Jon ha pedido cerveza
Sara ha pedido Coca-cola
- Con hielo
- Con limón
```

En el ejemplo, los **args* son *"hielo"* y *"limón"* del segundo pedido, pudiendo añadirse más si fuera necesario.

**- Arbitrary Keyword Arguments o Argumentos de palabras clave arbitrarias**
<br>
También llamados ***kwargs*, se diferencia de los **args* porque éstos recopilan múltiples argumentos posicionales en una tupla, mientras que los ***kwargs* recopilan argumentos de palabras clave en un diccionario.

*Ejemplo:*
```
def pedido(nom_cliente, tipo_pedido, **kwargs):
  print(nom_cliente, "ha pedido", tipo_pedido)
  for key, value in kwargs.items():
    print("- Añade", key, ":", value)

pedido("Jon", "sopa")
pedido("Sara", "hamburguesa", extras="huevo")
pedido("Helena", "plato combinado", extras="huevo", bebida="Coca-cola")
```
*Resultado:*
```
Jon ha pedido sopa
Sara ha pedido hamburguesa
- Añade extras : huevo
Helena ha pedido plato combinado
- Añade extras : huevo
- Añade bebida : Coca-cola
```
Ambos se pueden combinar en una misma función para que ésta sea más flexible, teniendo siempre en cuenta que los *args* deben indicarse antes que los **kwargs.

*Ejemplo:*
```
def pedido(nom_cliente, tipo_pedido, *args, **kwargs):
  print(nom_cliente, "ha pedido", tipo_pedido)
  for arg in args:
    print("- Añade", arg)
  for key, value in kwargs.items():
    print("- Añade", key, ":", value)
  
pedido("Helena", "plato combinado", "huevo", "mayonesa", bebida="Coca-cola")
```
*Resultado:*
```
Helena ha pedido plato combinado
- Añade huevo
- Añade mayonesa
- Añade bebida : Coca-cola
```


## ¿Qué es una función Lambda en Python?
Es una función anónima pequeña que puede aceptar cualquier número de argumentos, pero solo puede tener una expresión.
<br>
Por lo tanto, las funciones lambda pueden definirse y luego pasarse a otra función en un solo paso, sin necesidad de darles un nombre (por eso también se denominan funciones anónimas). Lambda es una función práctica que facilita la definición de funciones pequeñas y puntuales.

*Ejemplo:*
```
menú = lambda comida, complemento, bebida: f'{comida} {complemento} {bebida}'


def pedido(completo):
  print(f'Quiero mi {completo}!')

pedido(menú('bistec', 'con patatas', "y Coca-cola"))
```
*Resultado:*
```
Quiero mi bistec con patatas y Coca-cola!
```

## ¿Qué es un paquete pip?
PIP es un gestor de paquetes para paquetes/módulos de Python.
<br>
Un paquete contiene todos los archivos necesarios para un módulo, y éstos son bibliotecas de código de Python que puedes incluir en un proyecto.
<br>
Para instalarlo basta con seguir las instrucciones de su página oficial:

[https://pip.pypa.io/](https://pip.pypa.io/en/stable/installation/)

![Imagen_pypa](/Users/juditvega/Desktop/Cursos/programacion_2/checkpoints/checkpoint_5/images/pypa_img.png)

Una vez instalado, se puede comprobar su versión de la siguiente manera:

![Imagen_version](/Users/juditvega/Desktop/Cursos/programacion_2/checkpoints/checkpoint_5/images/pip_version.jpeg)

Con PIP podrán instalarse paquetes así:
```
C:\Users\TuNombre\AppData\Local\Programs\Python\Python36-32\Scripts>pip install camelcase
```
