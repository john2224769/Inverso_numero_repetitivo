# Programa N. 6. repetivivos: Hacer el diagrama de flujo y programa en python que lea un entero positivo de cualquier cantidad de cifras, que calcule su inverso y 
# lo imprima junto con el original 

from os import system
print("\n---------------------------------------------------------------------------")
print("---------------- Calcular el inverso de un numero  ------------------------")
print("---------------------------------------------------------------------------\n")

# input
n=int(input("\n Ingrese el numero para evaluar su inverso: "))

# processing
num=0
origin=n

while n>0:
    digito=n%10
    num=(num*10)+digito
    n=n//10

#output
print("\nEl numero invertido de "+str(origin)+", es: "+str(num))
print(" ")
