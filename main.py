<<<<<<< HEAD
from Escuderia import Escuderia 

escuderias=[]

numeroEscuderias=0
sumatoriaDeSalarios=0
while(numeroEscuderias < 2):
    escuderia = Escuderia()
    escuderia.nombre=input("Digita el nombre de la escuderia")
    escuderia.motor=input("digitel el motor de la escuderia ")
    escuderia.costoAnual=int(input("digite el costo anual"))
    #escuderia.piloto1.nombre=input("digite el nombre del piloto")
    #escuderia.piloto2.nombre=input("digite el nombre del piloto")
    escuderia.piloto1.salarioAnual=int(input("digital el salario del pilot1"))
    escuderia.piloto2.salarioAnual=int(input("digital el salario del pilot2"))
    escuderias.append(escuderia)
    numeroEscuderias+=1

for escuderia in escuderias:
    sumatoriaDeSalarios=sumatoriaDeSalarios+escuderia.piloto1.salarioAnual+escuderia.piloto2.salarioAnual
print(f"la sumatoria del salario de los pilotos de la escuderia es: {sumatoriaDeSalarios}")
=======
from Escuderia import Escuderia

escuderias=[]

numeroEscuderia=0
sumatoriaSalarios=0

while(numeroEscuderia<2):
    escuderia=Escuderia()
    escuderia.nombre=input("Digite el nombre de la escuderia: ")
    escuderia.motor=input("Digite el motor de la escuderia: ")
    escuderia.costoAnual=input("Digite el costo anual: ")
    escuderia.piloto1.salarioAnual=int(input("Digita el salario del piloto1: "))
    escuderia.piloto2.salarioAnual=int(input("Digita el salario del piloto2: "))
    
    escuderias.append(escuderia) #agregar la escuderia a la lista
    numeroEscuderia+=1
    
#recorrer la lista de esciderias
for escuderia in escuderias:
    #print(f"{escuderia.nombre}")
    sumatoriaSalarios=sumatoriaSalarios+escuderia.piloto1.salarioAnual+escuderia.piloto2.salarioAnual
    print(f"El salario acumulado fue: {sumatoriaSalarios}")
>>>>>>> 760c64d2d84c8e70da177e62bf9cd425fabace50
