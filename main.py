import os
from random import randint
def exibir(t):
    os.system("clear")
    print('\n | 1 | 2 | 3 |')
    for i in range(3):
        print(str(i+1)+'|', end='')
        for j in range(3):
            if(t[i][j] == 0):
                print(' _ |', end='')
            elif(t[i][j] == 1):
                print(' X |', end='')
            elif(t[i][j] == -1):
                print(' O |', end='')
        print()
def final(t):
    for i in range(3):
        t1 = t[i][0] + t[i][1] + t[i][2]
        t2 = t[0][i] + t[1][i] + t[2][i]
        if(t1 == 3):
            print('\nX vencedor.')
            return False
        elif(t1 == -3):
            print('\nO vencedor.')
            return False
        elif(t2 == 3):
            print('\nX vencedor.')
            return False
        elif(t2 == -3):
            print('\nO vencedor.')
            return False
    t3 = t[0][0]+t[1][1]+t[2][2]
    t4 = t[0][2]+t[1][1]+t[2][0]
    if(t3 == 3):
        print('\nX vencedor.')
        return False
    elif(t4 == 3):
        print('\nX vencedor.')
        return False
    elif(t3 == -3):
        print('\nO vencedor.')
        return False
    elif(t4 == -3):
        print('\nO vencedor.')
        return False
    return True
def jogador(t, v):
    while(True):
        l = int(input('Linha: '))
        j = int(input('Coluna: '))
        if(l < 1 or l > 3 or j < 1 or j > 3):
            print('Movimento Invalido.\n')
        elif(t[l-1][j-1] == 0):
            t[l-1][j-1] = v
            return t
        else:
            print('Movimento Invalido.\n')
def maquina(t, v):
    for i in range(3):
      t1 = t[i][0] + t[i][1] + t[i][2]
      t2 = t[0][i] + t[1][i] + t[2][i]
      if(t1 == v*2):
        for ii in range(3):
          if(t[i][ii] == 0):
            t[i][ii] = v
            return t
      elif(t2 == v*2):
        for ii in range(3):
          if(t[ii][i] == 0):
            t[ii][i] = v
            return t
    for i in range(3):
      t1 = t[i][0] + t[i][1] + t[i][2]
      t2 = t[0][i] + t[1][i] + t[2][i]
      if(t1 == -v*2):
        for ii in range(3):
          if(t[i][ii] == 0):
            t[i][ii] = v
            return t
      elif(t2 == -v*2):
        for ii in range(3):
          if(t[ii][i] == 0):
            t[ii][i] = v
            return t
    t3 = t[0][0]+t[1][1]+t[2][2]
    t4 = t[0][2]+t[1][1]+t[2][0]
    if(t3 == 2 or t3 == -2):
        if(t[0][0] == 0):
            t[0][0] = v
        elif(t[1][1] == 0):
            t[1][1] = v
        elif(t[2][2] == 0):
            t[2][2] = v
        return t
    elif(t4 == 2 or t4 == -2):
        if(t[0][2] == 0):
            t[0][2] = v
        elif(t[1][1] == 0):
            t[1][1] = v
        elif(t[2][0] == 0):
            t[2][0] = v
        return t
    elif(t[1][1] == 0):
        t[1][1] = v
        return t
    elif(t[0][0] == -v and t[2][2] == 0):
        t[2][2] = v
        return t
    elif(t[2][2] == -v and t[0][0] == 0):
        t[0][0] = v
        return t
    elif(t[2][0] == -v and t[2][0] == 0):
        t[0][2] = v
        return t
    elif(t[0][2] == -v and t[2][0] == 0):
        t[2][0] = v
        return t
    elif(t[0][2] == 0 and t[0][2] == 0):
        t[0][2] = v
        return t
    elif(t[2][2] == 0):
        t[2][2] = v
        return t
    elif(t[2][0] == 0):
        t[2][0] = v
        return t
    elif(t[0][0] == 0):
        t[0][0] = v
        return t
    elif(t[0][2] == 0):
        t[0][2] = v
        return t
    while(True):
        i = randint(0,2)
        j = randint(0,2)
        if(t[i][j] == 0):
            t[i][j] = v
            return t
def jogo():
    t = [[0,0,0],
        [0,0,0],
        [0,0,0]]
    j = 0
    exibir(t)
    while(final(t)):
        if(j == 9):
            exibir(t)
            print('\nEmpate.')
            break
        j += 1
        if(j%2 != 0):
            print('\nJogador X: \n')
            t = maquina(t, 1) # É possivel trocar 'maquina()' por 'jogador()'
        else:
            print('\nJogador O: \n')
            t = jogador(t, -1) # É possivel trocar 'jogador()' por 'maquina()'
        exibir(t)
    print(str(j)+' jogadas.')
jogo()