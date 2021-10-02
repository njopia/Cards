import random
import os
import time
os.system("cls")

#Ciclo que genera una lista aleatoria de números trampa
listaTrampa=[]
for i in range (0,12):
    listaTrampa.append(random.randint(1,101))
    
#print(listaTrampa)

listaIntentos=[]
intentos=0
listaPosicion=[]

sumatoria=0 #esta variable se queda afuera del bucle para mantener el último dato intacto.

devMode=False #Habilita el Modo developer (Mostrar valores ocultos)
victory=False 
passw=1881
devTag="[DEV]"
errorTag="[ERROR]"

while True:
    print("Bienvenido a JUMANJI") 
    nombreJugador=input("Ingrese nombre de jugador:   ")
    if nombreJugador.isalpha() == False:
        print("Solo se permiten letras... \n")
        time.sleep(2)
    else:
        break

            
def mostrarResumen():
    print("\n \n")
    print("RESUMEN DE LA PARTIDA: \n")
    print(f"Nombre de Jugador: {nombreJugador}")
    if victory==True:
        print("El usuario a GANADO la partida")
    else:
        print("El usuario ha PERDIDO la partida")
    print(f"Intentos realizados: {intentos}")        

    print("Listado de dados: ", listaIntentos)
    print("Posición de casillas por ronda: ", listaPosicion)
    print(f"Casilla final: {sumatoria}")
    print(f"Listado Trampas: {listaTrampa}")    
    print("\n \n")
   
while True:
    if devMode==True:
        print(f"{devTag} Listado números trampa:",listaTrampa)
        print(f"{devTag} Contraseña de salida:",passw)          
    continuar=int(input(("\033[0;92m"+f"\n Casilla actual: ({sumatoria}) \n \n Lanzar nuevamente: \n \n 1: SI \n 2: NO \n \n"+"\033[0m")))
        
    if continuar == 1:
        magia=random.randint(1,6)
        listaIntentos.append(magia)
        sumatoria=sumatoria+magia
        intentos=intentos+1
        listaPosicion.append(sumatoria)
        
        #mostrarResumen()
        if sumatoria > 101:
            print("Limite alcanzado:   GANASTE!!", sumatoria)
            time.sleep(3)
            victory=True
            mostrarResumen()
            break
        elif magia in listaTrampa:
            print("[¡¡¡BOOM!!!] El cazador te ha pillado. \n Fin de la película...!!!")
            time.sleep(3)
            mostrarResumen()
            break
            
    elif continuar == 2:
        password=int(input("Ingrese contraseña:   "))
        if password == passw:
            print("Gracias por jugar")
            time.sleep(3)
            mostrarResumen()
            break
        else:
            print(("\033[0;91m"+f"\n {errorTag}****CONTRASEÑA INCORRECTA****\nVolviendo al juego..."+"\033[0m"))#Colorear Texto
            time.sleep(3)
    else:
        print(f"\n \n {errorTag}Comando incorrecto. Ingrese valores entre 1 y 2...")
        time.sleep(3)
