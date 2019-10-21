#Hacer que el sistema genere un ejercicio
#aleatorio entre 1 y 10. Luego de hacer 
#que el ususario adivine el número. La
#aplicacion debe terminar cuando el usuario 
#adivine.

import random
os.system ("cls")

s = random.randint(1,10)

while True:
    n = int(input("Adivina el número del sistema (1,10):"))
    
    if n == s:
        print ("Adivinaste!")
        break
    else:
        print("Número incorrecto")