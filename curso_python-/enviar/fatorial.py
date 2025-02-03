

numero = int(input("digite um numero que vai ser calculado: "))

fatorial = 1

contador = numero

while contador > 1:
    fatorial = fatorial * contador
    contador = contador - 1
    
print(fatorial)
