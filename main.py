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