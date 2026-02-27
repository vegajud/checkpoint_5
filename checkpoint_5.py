#Cree un bucle For de Python.

for num in range(1, 76):
  print(num)

#Cree una función de Python llamada suma que tome 3 argumentos y devuelva la suma de los 3.
  
  def suma (num1, num2, num3):
    return num1 + num2 + num3

  print(suma(5,10,15))

#Cree una función lambda con la misma funcionalidad que la función de suma que acaba de crear. 

suma_lambda = lambda num1, num2, num3: num1 + num2 + num3
print(suma_lambda(5,10,15))


#Utilizando la siguiente lista y variable, determine si el valor de la variable coincide o no con un valor de la lista:  

lista_nombre = 'Jessica', 'Paul', 'George', 'Henry', 'Adán'

nombre = 'Enrique' 

if nombre in lista_nombre:
    print('El nombre está en la lista')
else:
    print('El nombre no está en la lista')
