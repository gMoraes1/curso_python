#criar o jogo do NIM com o computador   
# vai ter 3 funções, computador_escolhe_jogada, usuario_escolhe_jogada e partida    
# n= numero de peças inicial, m= numero maximo de peças que podem ser retiradas por jogada
def computador_escolhe_jogada(n,m):
    if n <= m:
        return n
    else:
        if n % (m+1) > 0:
            return n % (m+1)
        return m    

def usuario_escolhe_jogada(n,m):
    jogada = int(input("Quantas peças você vai tirar ?"))
    while jogada > m or jogada <= 0 or jogada > n:
        print("Jogada inválida")
        jogada = int(input("Quantas peças você vai tirar ?"))   
        return jogada

def partida():
    n = int(input("Quantas peças ?"))
    m = int(input("Limite de peças por jogada ?"))
    if n % (m+1) == 0:
        print("Você começa !")
        while n > 0:
            jogada = usuario_escolhe_jogada(n,m)
            n = n - jogada
            print("Você tirou", jogada, "peças")
            print("Restam", n, "peças")
            if n == 0:
                print("Você ganhou !")
                return 0
            jogada = computador_escolhe_jogada(n,m) 
            n = n - jogada  
            print("O computador tirou", jogada, "peças")
            print("Restam", n, "peças")
            if n == 0:
                print("O computador ganhou !")
                return 1
    else:
        print("Computador começa !")
        while n > 0:
            jogada = computador_escolhe_jogada(n,m) 
            n = n - jogada
            print("O computador tirou", jogada, "peças")
            print("Restam", n, "peças")
            if n == 0:
                print("O computador ganhou !")
                return 1
            jogada = usuario_escolhe_jogada(n,m)
            n = n - jogada
            print("Você tirou", jogada, "peças")
            print("Restam", n, "peças")
            if n == 0:
                print("Você ganhou !")
                return 0     
partida()
def campeonato():
    rodada = 1
    while rodada <= 3:
        print("**** Rodada", rodada, "****")
        partida()
        rodada = rodada + 1
    print("**** Final do campeonato ! ****")
    print("Placar: Você 0 X 3 Computador")              
   

