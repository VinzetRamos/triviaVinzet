BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'
import random 
import time

import time  


puntaje = random.randint(0, 3)

print (RED+"Bienvenido a mi trivia  "+RESET)

for numero_carga in range(5,0,-1):
  time.sleep(1)
  print(numero_carga)


print ("\nPondremos a prueba tus conocimientos en 2 partes")
print ("\nTienes a tu favor ", puntaje, "puntos")



nombre = input (GREEN+"\nIngresa tu nombre: "+RESET)
time.sleep(1)

print ("\n Hola",GREEN+ nombre +RESET, "responde las siguientes preguntas \n escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")
time.sleep(1)

print("\nA esta preguntara se te agregara el pintaje aleatorio y se te dará o quitara puntos dependiendo a tu respuesta")
print (BLUE+"\n1)¿En que lenguaje de programación se progamó Gmail?"+RESET)
time.sleep(1)
print ("\na) Python")
print ("b) Java")
print ("c) PHP")
print ("d) Assembly")

respuesta_3 = input("\nTu respuesta: ")
time.sleep(1)

while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")
  time.sleep(1)

if respuesta_3 == "a":
  print ("Totalmente incorrecto! tienes obtienes un punto menos")
  puntaje_1 = puntaje - 1
  print ("Tienes",puntaje_1,"puntos")
elif respuesta_3 == "d":
  print ("Por poco :( obtuviste 5 puntos")
  puntaje_1 = puntaje + 5
elif respuesta_3 == "c":
  print ("Incorrecto! no se te otorgo puntos")
  puntaje_1 = puntaje + 0
else:
  print ("Correcto! obtienes 8 puntos")
  puntaje_1 = puntaje + 8

time.sleep(1)
print (" tienes", puntaje_1,"puntos")

time.sleep(1)
print("\nEsta pregunta es todo o nada")
print(BLUE+"\nAhora ingresa 2 numeros que multipicados sean '25'"+RESET)

x = int(input("Primer numero: "))
z = int(input("Segundo numero: "))
respuesta = x * z


if respuesta == int(25):
  print("correcto obtuviste 10 puntos")
  puntaje_3 = int(10)
  print("tu puntaje total fue de", puntaje_1 + puntaje_3)
else:
  print("incorrecto obtuviste 0 puntos")
  puntaje_3 = int(0)
  print("tu puntaje total fue de: ",puntaje_1 )

print(BLUE+"\n Ahora obtendremos tu promedio siendo 10 la nota máxima y 0 la mínima"+RESET)
time.sleep(1)
a = int(input("\nIngresa tu primer puntaje: "))
time.sleep(1)
if a == puntaje_1:
  print("correcto")
  
  
else:
  print("\nIngresa tu puntaje que obtuviste, no seas tramposo")
  a = int(input("Ingresa tu primer puntaje: "))
  
b = int(input("Ingresa tu segundo puntaje: "))
if b == puntaje_3:
  print("Correcto")
else:
  print("Ingresa tu segundo puntaje no seas tramposo")
  b = int(input("ingrea tu segundo puntaje: "))
time.sleep(1)
print("\nTu puntaje final es: ", (a+b)/2, "puntos")
print("GRACIAS", nombre, "por participar en la primera parte de mi trivia!")



print(RED+"\nAhora sigamos con la siguiente parte"+RESET)

for numero_carga1 in range (3,0,-1):
  time.sleep(1)
  print(numero_carga1)  

puntaje1 = 0
trivia_2 = True
intentos = 0
print("\nEn esta parte podras intentar las veces que quieras")
print("\n¡a por elló")

while trivia_2 == True:
  intentos +=1
  puntaje1=0

  print(BLUE+"\nEn que año fue la guerra del pacífico"+RESET)
  GUERRA =  [1888,1881,1882,1879]

  for año in range (0,4):
    print("*",GUERRA[año])
    
  año = input()
  while año not in ("1888","1881","1882","1879"):
    print("debes colocar una de las alternativas")
    año = input()
    
  if año == "1879":
    puntaje1 = puntaje1 +10
    print("Correcto obtuviste", puntaje1)
  else:
    print("incorrecto obtuviste: ", puntaje1)

  
    
      

  print("\n¿Deseas intentar la trivia nuevamente?")
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()

  if repetir_trivia != "si":  
   print("\nEspero",nombre, "que lo hayas pasado bien, hasta pronto!","tus intentos fueron",intentos)
   trivia_2 = False  






