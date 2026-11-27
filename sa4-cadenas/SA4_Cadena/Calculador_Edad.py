import datetime as dt
import math

hoy = dt.datetime.now()
deltahoy = dt.timedelta(
    days=(int(hoy.strftime('%Y'))*365 + math.floor(int(hoy.strftime('%Y'))/4)  + int(hoy.strftime('%j'))),
    hours=int(hoy.strftime('%H')),
    minutes=int(hoy.strftime('%M')),
    seconds=int(hoy.strftime('%S'))
)

nacimiento = dt.datetime.strptime(input("Escriba su fecha de nacimiento en formato dd/mm/aaaa. "), "%d/%m/%Y")
deltanacimiento = dt.timedelta(days=(int(nacimiento.strftime('%Y'))*365 +math.floor(int(nacimiento.strftime('%Y'))/4)  + int(nacimiento.strftime('%j'))))
deltaedad = deltahoy - deltanacimiento

print(f"Entonces usted lleva vivo {round(deltaedad.days/365.25, 2)} años en total.")
print(f"Entonces usted lleva vivo {round(deltaedad.days/30.4375, 2)} meses en total.")
print(f"Entonces usted lleva vivo {round(dt.timedelta.total_seconds(deltaedad)/3600, 2)} horas en total.")
print(f"Entonces usted lleva vivo {dt.timedelta.total_seconds(deltaedad)} segundos en total.")
