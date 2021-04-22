print('------Hoja de trabajo 2-------')
print('#########Ejercicio 1##########')
triangulo=int(input("Ingrese un número entero:"))
o=""
for i in range (0, triangulo, 1):
  o=o+"*"
  print(o) 
print('##########Ejercicio 2#########')
numero=int(input("Ingrese un número entero:"))
if numero>=0:
    if numero % 2 ==0:
        print('El número no es primo ')
    else:
        print('El número es primo')
else: 
    print('El número debe de ser entero positivo')