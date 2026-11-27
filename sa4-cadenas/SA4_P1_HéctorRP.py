#Ej1
animal = input("Hola, buenos días. Dígame el nombre de un animal. ")
print(animal+animal+animal+animal+animal)
print(animal*5)

#Ej2
autor = input("Dígame el nombre de un autor español. ")
n = int(input("Y dígame también un número entero. "))
print(autor[1])
print(autor[-2])
print(autor[:n])
print(autor[-n:])
print(autor[2:n+2])  #print(autor[3:n+2])
print(autor[::2])
print(autor[1::2][::-1])  #print(autor[::-1])

#Ej3
num_real = float(input("Ahora, por favor, dime un número real. "))
print(str(num_real) + " + 4 = " + str(num_real+4))
print(f"{num_real:.2f} * {3.37:.2f} " + f" = {num_real * 3.37:.4f}") #" = "
print(num_real, " / 2 = ",  num_real/2)
print(f"{num_real}", " % 3 = " + str(num_real%3))

#Ej4
bool1 = bool(int(input("Dime el valor de la primera variable booleana. 1 Para True y 0 para False. ")))
bool2 = bool(int(input("Dime el valor de la segunda variable booleana. 1 Para True y 0 para False. ")))
print(f"¿Son las dos variables True? {bool1 and bool2}.")
print(f"¿Es alguna de las dos variables True? {bool1 or bool2}.")

#Ej5
print(f"{'HéctorRP':;<20}")
print(f"{'HéctorRP':;^20}")
print(f"{'HéctorRP':;>20}")

#Ej6
poema = (
    "Caminante, son tus huellas \n"
    "\t el camino y nada más; \n"
    "Caminante, no hay camino, \n"
    "\t se hace camino al andar. \n"
    "Al andar se hace el camino, \n"
    "\t y al volver la vista atrás \n"
    "\t se ve la senda que nunca \n"
    "\t se ha de volver a pisar. \n"
    "Caminante no hay camino \n"
    "\t sino estelas en la mar. \n"
    )
print(poema)

