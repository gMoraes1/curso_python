def éprimo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):  
        if n % i == 0:
            return False
    return True

def maior_primo(n):
    for i in range(n, 1, -1): 
        if éprimo(i):
            return i
    return 2  
