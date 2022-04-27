from datetime import datetime, date
import time

fechaYHora = datetime.now()

print(fechaYHora)
print(time.strftime("%Y-%m-%d %H:%M:%S"))

año = fechaYHora.year
mes = fechaYHora.month
dia = fechaYHora.day

hora = fechaYHora.hour
min = fechaYHora.minute
seg = fechaYHora.second

print("Fecha: {}/{}/{}".format(dia, mes, año))
print("Hora: {}:{}:{}".format(hora, min, seg))
print("Año: {}".format(año))

dia_semana = fechaYHora.weekday()
print(dia_semana)
print(fechaYHora.isoweekday())

def esFinDeSemana():
    return date.today().weekday() > 4

if esFinDeSemana():
    print("conprar criptos")
