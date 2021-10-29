from datetime import datetime

fechaYHora = datetime.now()

print(fechaYHora)

año = fechaYHora.year
mes = fechaYHora.month
dia = fechaYHora.day

hora = fechaYHora.hour
min = fechaYHora.minute
seg = fechaYHora.second

print("Fecha: {}/{}/{}".format(dia, mes, año))
print("Hora: {}:{}:{}".format(hora, min, seg))
print("Año: {}".format(año))