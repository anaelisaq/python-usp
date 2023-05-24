segundos = int(input("Por favor, entre com o número de segundos que deseja converter: "))
dias = segundos // (24 * 3600)
segundos = segundos % (24 * 3600)
horas = segundos // 3600
segundos %= 3600
minutos = segundos // 60
segundos %= 60

print(dias,"dias,", horas, "horas,", minutos, "minutos e", segundos, "segundos.")