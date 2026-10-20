
#programa que permite vendedr bebidas
#solicita una opcion para elegir la bebida
#preguntas la cantidad de bebida
#Muestra total a pagar

print("Agua de litro 50 pesos")
print("Agua de jamaica ,1")
print ("Agua de Coco ,2")
print("Agua de Mango ,3")
A=int(input("Ingresa que agua quieres"))
B=int(input("Cuantos litros quieres"))

if opcion == 1:
    bebida = 'Agua de jamaica'
    precio = 25
elif opcion == 2:
    bebida = 'Agua de Coco'
    precio = 50
elif opcion == 3:
    bebida = 'Agua de Mango'
    precio = 20
else:
    bebida ='no existe bebida'
    precio = 0

if precio > 0:
    total = precio * A
    print(f"{A} de {bebida}")
    print(f"{A}")
    print(f"total a pagar: $ {total}")
else:
    print("no existe bebida")