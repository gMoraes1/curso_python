#excercicio de transformar os segundos digitados pelo usuario, em horas, minutos e segundos 

segundo = input("Digite os segundos a serem convertidos: ")

segundo_convertido = int(segundo)

hora = segundo_convertido// 3600
segundos_restantes = segundo_convertido % 3600
minutos = segundos_restantes //60
segundos_restantes_final = segundos_restantes % 60
dias = hora // 24
horas_restantes = hora % 24

print(f"Os dias totais são: {dias}, as horas restantes são: {horas_restantes}, os minutos são: {minutos}, e os segundos são: {segundos_restantes_final}.")
