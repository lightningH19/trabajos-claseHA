#Tarea1
print("Buenos días, soy Bellisarious Cawl, creado por Héctor Ramírez Penadés, soy tu asistente.")

#Tarea2
nombre_usuario = input("¿Usted cómo se llama? \n")
#Tarea2.1
print("Sea bienvenido ",nombre_usuario,". Tiene usted un nombre muy bonito, ¿sabe?", sep="")
#Tarea2.2
print(nombre_usuario, nombre_usuario, nombre_usuario, nombre_usuario, nombre_usuario, sep=", ", end=". \n")

#Tarea3
multiplos_numero = int(input("¿Sería tan amabe de decirme un número? Yo le diré sus 4 primeros múltiplos \n"))
print("Sus 4 primeros múltiplos son:")
print(multiplos_numero*2, multiplos_numero*3, multiplos_numero*4, multiplos_numero*5, sep="; ")

#Tarea4
operaciones_numero = float(input("Por favor, dígame otro número, haré unas operaciones con el \n"))
autopotencia = operaciones_numero ** operaciones_numero
division = operaciones_numero / multiplos_numero
print("Lo he elevado sobre si mismo y también lo he dividido entre el primer numero que me diste. Estas son las operaciones:")
print(operaciones_numero, "^", operaciones_numero, " = ", autopotencia)
print(operaciones_numero, " / ", multiplos_numero, " = ", division)

#Tarea5
print("Ahora necesito que me digas los valores de dos variables booleanas.")
bool1 = bool(int(input("Escribe 1 si quieres que su valor sea True o escribe 0 si quieres que su valor sea False. \n")))
bool2 = bool(int(input("Escribe 1 si quieres que su valor sea True o escribe 0 si quieres que su valor sea False. \n")))
booland = bool1 and bool2
print("¿Las dos variables son True?", booland)
boolor = bool1 or bool2
print("¿Alguna de las dos variables es True?", boolor)

print("Adios ", nombre_usuario, ". Que tenga usted un buen día.", sep="")
