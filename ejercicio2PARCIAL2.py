############ GUILLER SEBASTIAN LASSO RENDON ###############
########### FABIAN ANDRES ROSERO ALDANA #########
########### 3 SEMESTRE POE ##############


import random
def generar_rango():
    while True:
        try:
            dificultad = int(input("introduzca un numero maximo de rango: "))
            if dificultad <= 0 :
                print("error: elija un numero positivo mayor a 0")
                continue
            return dificultad
        except Exception as e:
            print("error: por favor elija un numero entero")

def obtener_numero():
            try:
                numero = input(f"introduzca un numero entre 1 y {numero_rango}: ")
                
                return numero
            except Exception as e:
                print("error: por favor elija un numero. ")
                

def pista(numero_adivinar, numero_introducido):
    if numero_introducido < numero_adivinar and isinstance(numero_introducido,int):
        print(f"fallaste el numero introducido es menor")

    elif numero_introducido > numero_adivinar and isinstance(numero_introducido,int):
        print(f"fallaste el numero introducido es mayor")
        
    
    else:
         print("")


numero_rango = generar_rango()
numero_intentos = 1 if numero_rango < 20 else numero_rango // 20

numero_adivinar = random.randint(1,numero_rango)

vector_palabras = ["fallo" for _ in range(numero_rango + 1)]
vector_palabras[numero_adivinar] = "acerto"


def jugar():
    
    intentos_restantes = numero_intentos
    for i in range(numero_intentos):
        print(f"intentos restantes {intentos_restantes}")
        numero = obtener_numero()

        if not numero.isdigit() and not isinstance(numero,int):
             print(" error no es un numero.")
             intentos_restantes -= 1
             continue
        else:
             numero = int(numero)
        
        if numero <= len(vector_palabras) and vector_palabras[numero] == "acerto":
            print(" ********** HAS ACERTADO FELICITACIONES ************** ")
            break
        else:
            intentos_restantes -= 1
        
        pista(numero_adivinar,numero)
    
    if intentos_restantes == 0 :
        print("**********  HAS PERDIDO ***********")


jugar()

