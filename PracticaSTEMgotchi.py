#====================================================#
#=====================Funciones======================#
#====================================================#

def contadoresDeEstado(contFeli,contComi,contCaca,enfermo):
    felicidad = "💗"
    comida = "🍕"
    caca = "💩"
    
    print(f"\nFelicidad: {felicidad*contFeli}")
    print(f"Comida: {comida*contComi}")
    print(f"Caca: {caca*contCaca}")
    if contadorCaca >= 3:
        enfermo = True
        print(f"¿Esta enfermo? {enfermo}")
    else:
        print(f"¿Esta enfermo? {enfermo}")

def infoStemgotchi(nombre,peso):
    print(f"\nTu STEMgotchi se llama: {nombre}")
    print(f"Tu STEMGgotchi pesa: {peso}L ")

def contarLetras(nombre):
    contadorLetras = 0
    for letra in nombre:
        contadorLetras += 1
    return contadorLetras

#====================================================#
#==================Codigo=Principal==================#
#====================================================#

#====================Contadores======================#

nombreStemgotchi = input("\nEscribe el nombre de tu STEMgotchi --> ")
while contarLetras(nombreStemgotchi) >= 5:
    nombreStemgotchi = input("\nEscribe el nombre de tu STEMgotchi --> ")


contadorFelicidad = 0
contadorComida = 0
contadorCaca = 0

enfermo = False
peso = 1
tiempo = 0

contadoresDeEstado(contadorFelicidad,contadorComida,contadorCaca,enfermo)

#====================Contadores======================#

#======================Bucle=========================#

bucle = True

while bucle != False:
    accionARealizar = int(input("""
1. Info STEMgotchi
2. Comer
3. Jugar 
4. Limpiar Caca
5. Curar a STEMgotchi
6. SALIR de STEMgotchi
                                
Escribe que accion quieres realizar --> """))

#======================Comer=========================#
    if accionARealizar == 2:
        if contadorCaca == 0 and enfermo == False:
            seleccion = int(input("""
Puedes darle de comer: 
1. Comida 🍙
2. Dulce 🍡 
Escribe que quieres darle de comer a tu STEMgotchi --> """))
            if seleccion == 1:
                contadorComida += 1
                peso += 1
            if seleccion == 2:
                contadorComida += 1
                contadorFelicidad += 1
                peso += 2
            tiempo += 1
        else:
            print("No puedes comer! tienes cacas!")
#======================Comer=========================#

#======================Jugar=========================#
    if accionARealizar == 3:
        if contadorCaca < 3 and enfermo == False:
            print("vamos a jugar 🕹️ :D ")
            contadorFelicidad += 1
            contadorComida -= 1
            peso -= 1
            tiempo += 1
        else:
            print("No puedes jugar tienes demasiado")
#======================Jugar=========================#

#====================Limpiar=Caca====================#
    if accionARealizar == 4:
        contadorCaca = 0
#====================Limpiar=Caca====================#

#======================Tiempo========================#
    if tiempo == 3:
        contadorCaca += 1
        contadorFelicidad -= 1
        tiempo = 0
#======================Tiempo========================#

#=====================Enfermar=======================#
    if contadorCaca == 3:
        enfermo = True
#=====================Enfermar=======================#

#=======================Curar========================#
    if accionARealizar == 5:
        if contadorCaca < 3:
            enfermo = False
        else:
            print("\nTienes cacas no puedes :(")
#=======================Curar========================#

#================Restriccion=Contador================#
    if contadorFelicidad > 4:
        contadorFelicidad = 4
    elif contadorFelicidad < 0:
        contadorFelicidad = 0

    if contadorComida > 4:
        contadorComida  = 4
    elif contadorComida < 0:
        contadorComida  = 0

    if contadorCaca > 6:
        contadorCaca = 6
    if contadorCaca < 0:
        contadorCaca = 0

    if peso > 99:
        peso = 99
    if peso < 0:
        peso = 0
#================Restriccion=Contador================#

#=======================EXIT=========================#
    if accionARealizar == 6:
        bucle = False
#=======================EXIT=========================#

    contadoresDeEstado(contadorFelicidad,contadorComida,contadorCaca,enfermo)

#======================INFO==========================#
    if accionARealizar == 1:
        infoStemgotchi(nombreStemgotchi,peso)
#======================INFO==========================#

#======================Bucle=========================#