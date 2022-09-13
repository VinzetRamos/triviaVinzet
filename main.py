import random  

puntaje = random.randint(0, 3)

print ("Bienvenido a mi trivia  ")
print ("Pondremos a prueba tus conocimientos en 2 preguntas")
print ("Tienes a tu favor ", puntaje, "puntos")



nombre = input ("Ingresa tu nombre: ")


print ("\n Hola", nombre, "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n")


print ("\n1) ¿En que lenguaje se progamó Gmail?")
print ("a) Python")
print ("b) Java")
print ("c) PHP")
print ("d) Assembly")

respuesta_3 = input("\nTu respuesta: ")

while respuesta_3 not in ("a", "b", "c", "d"):
  respuesta_3 = input ("Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: ")

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


print (" tienes", puntaje_1,"puntos")


print("\nEsta pregunta es todo o nada")
print("Ahora ingresa 2 numeros que multipicados sean '25'")

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

print("\n Ahora obtendremos tu promedio siendo 10 la nota máxima y 0 la mínima")

a = int(input("Ingresa tu primer puntaje: "))

if a == puntaje_1:
  print("correcto")
  
  
else:
  print("Ingresa tu puntaje que obtuviste, no seas tramposo")
  a = int(input("Ingresa tu primer puntaje: "))
  
b = int(input("Ingresa tu segundo puntaje: "))
if b == puntaje_3:
  print("Correcto")
else:
  print("Ingresa tu segundo puntaje no seas tramposo")
  b = int(input("ingrea tu segundo puntaje: "))

print("Tu puntaje final es: ", (a+b)/2, "puntos")
print("GRACIAS", nombre, "por participar de mi trivia!")


  






