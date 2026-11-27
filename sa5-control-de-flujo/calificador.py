nota = float(input("Escriba la nota del alumno: "))
print("las notas se redondean.")

if nota < 5:
    print(f"Ha sacado un {round(nota, 0)}, insuficiente.")
elif round(nota, 0) == 5:
    print(f"Ha sacado un {round(nota, 0)}, suficiente.")
elif round(nota, 0) == 6:
    print(f"Ha sacado un {round(nota, 0)}, bien.")
elif 6 < round(nota, 0) < 9:
    print(f"Ha sacado un {round(nota, 0)}, notable.")
else:
    print(f"Ha sacado un {round(nota, 0)}, sobresaliente.")