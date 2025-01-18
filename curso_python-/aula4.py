a = float(input("digite o valor para a: "))
b = float(input("digite o valor para b: "))
c = float(input("digite o valor para a: "))

delta = b**2 - 4*a*c
print(delta)

if delta < 0:
    print("nao existe raiz real para esse numero")
elif delta == 0:
    x = -b / (2*a)
    print("a raiz dessa equação é: ", x)      
else: 
    x1 = (-b + delta**0.5) / (2*a)
    x2 = (-b - delta**0.5) / (2*a)
    print("as raizes dessa equação são: ", x1, "e", x2)

















#colinha delta = b**2 - 4*a*c    
# resolução da equação de segundo grau  
# x = (-b +- delta**0.5) / 2*a  