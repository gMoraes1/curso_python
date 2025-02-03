#ordem crescente
numero = float(input("digite um numero com 3 casas: ")) 


if numero % 10 > (numero // 10) % 10 and (numero // 10) % 10 > numero // 100:
    print("crescente")  
else:
    print("não está em ordem crescente")    