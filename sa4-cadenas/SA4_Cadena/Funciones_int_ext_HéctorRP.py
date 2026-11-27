import os
import time
import unicodedata as uni
import math
import datetime as dt
import calendar as cl
import random


#Ejer1
path = os.path.abspath(__file__)
print(f" Este archivo se llama {os.path.basename(path)}, está en la ruta {path} y fue creado por Héctor Rayo.")

#Ejer2
print(f"{'Carácter':<7} {'Código':^8} {'Nombre':>9}")
print(f"{'0':<7} {ord('0'):^12} {uni.name('0')}")
print(f"{'A':<7} {ord('A'):^12} {uni.name('A')}")
print(f"{'a':<7} {ord('a'):^12} {uni.name('a')}")
print(f"{'à':<7} {ord('à'):^12} {uni.name('à')}")
print(f"{'á':<7} {ord('á'):^12} {uni.name('á')}")
print(f"{'ñ':<7} {ord('ñ'):^12} {uni.name('ñ')}")
print(f"{'ç':<7} {ord('ç'):^12} {uni.name('ç')}")
print(f"{'🙂':<6} {ord('🙂'):^12} {uni.name('🙂')}")
print(f"{'👍':<6} {ord('👍'):^12} {uni.name('👍')}")

#Ejer3
color1, color2 = input("Dígame el nombre un color. "), input("Dígame el nombre de otro color. ")
print(f"¿Es el primer color mayor alfabéticamente que el segundo? {color1.lower() > color2.lower()}.")
print(f"¿Es el primer color menor alfabéticamente que el segundo? {color1.lower() < color2.lower()}.")
print(f"¿Es el primer color igual alfabéticamente que el segundo? {color1.lower() == color2.lower()}.")

#Ejer4
num_dec = float(input("Escriba un número con dos decimales. "))
print(num_dec)
print(round(num_dec, 1))
print(round(num_dec, 0))
print(round(num_dec, -1))
print(round(num_dec, -2))
print(num_dec * -1)
print(abs(num_dec))
print(math.ceil(num_dec))
print(math.floor(num_dec))

#Ejer5
hoy = dt.datetime.now()
print(f"La fecha y hora actuales de este maravilloso día son  {hoy.strftime('%d/%m/%Y %I : %M %p')}.")

#Ejer6
nacimiento = dt.date(int(input("¿En que año nació? ")), int(input("¿En que mes nació? ")), int(input("¿En que día nació? ")))
print(f"Entonces usted nació en el {nacimiento.strftime('%d/%m/%Y')}. ")

#Ejer7
calendario = cl.LocaleTextCalendar(locale="es_ES.utf-8")
calendario.prmonth(int(hoy.strftime('%Y')), int(hoy.strftime('%m')))

#Ejer8
print(f"Este sistema operativo es {os.uname().sysname} y su núcleo es {os.name}.")

#Ejer9
limpiador = input("Pulse intro para limpiar la pantalla. ")
os.system("clear")

#Ejer10
limite = int(input("Introduzca un número entero superior a 50. "))
print(f"Un número aleatório desde el uno al que has introducido sería {random.randint(1, limite)}. ")
