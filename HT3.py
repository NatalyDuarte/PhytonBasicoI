print("------Hoja de trabajo 3-------")
print("#########Ejercicio 1##########")
contra1=input("Ingrese una contraseña:")
contra2=input("Vuelva a ingresar la contraseña:")
if contra1.lower() == contra2.lower():
    print("Las contraseñas coinciden")
else:
    print("Las contraseñas no coinciden")
print('#########Ejercicio 2##########')
Nombre=input("Ingrese su nombre:")
Sexo=input("Ingrese su sexo, M si es mujer y H si es hombre:")
if (Sexo == "M" and Nombre.lower() <"m") or (Sexo  == "H" and Nombre.lower() >"n") :
    print("Corresponde al grupo A")
else:
    print("Corresponde al grupo B")
