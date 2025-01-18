#agora verificar se o numero é divisivel por 3 e por 5  

numero = float(input("digite um numero: ")) 

if numero % 3 == 0 and numero % 5 == 0:
    print("FizzBuzz")
else:
    print(numero)

    