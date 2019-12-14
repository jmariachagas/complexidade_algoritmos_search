import numpy as np
import timeit
import random

A = []
V = []

item = 0

def sorteio_numero(A):
    item = random.choice(A)
    return item

def pesquisa_linear(A, item):

    for x in range(len(A)):
        if A[x] == item:
            return x

def embaralha_vetor(A):
    A = random.shuffle(A)
    return A

num = 1000

while(num != 0):
    A = np.arange(0, num, 1)
    for z in range(0,5):
        embaralha_vetor(A)
        total = 0
        for x in range(0,1000):
            item = sorteio_numero(A)
            timeit.default_timer
            total += timeit.timeit("pesquisa_linear(A, item)", "from __main__ import pesquisa_linear, A, item", number=1)
        V.append(total)
    if num == 1000:
        arquivo = open("arquivo_pl_1000.txt", "a")
        for y in range(0, 5):
            arquivo.write(str(V[y]) + '\n')
        print V
        V = []
    elif num == 4000:
        arquivo = open("arquivo_pl_4000.txt", "a")
        for y in range(0, 5):
            arquivo.write(str(V[y]) + '\n')
        print V
        V = []
    elif num == 5000:
        arquivo = open("arquivo_pl_5000.txt", "a")
        for y in range(0, 5):
            arquivo.write(str(V[y]) + '\n')
        print V
        V = []
    elif num == 6000:
        arquivo = open("arquivo_pl_6000.txt", "a")
        for y in range(0, 5):
            arquivo.write(str(V[y]) + '\n')
        print V
        V = []
    elif num == 10000:
        arquivo = open("arquivo_pl_10000.txt", "a")
        for y in range(0, 5):
            arquivo.write(str(V[y]) + '\n')
        print V
        V = []
    num = int(input("Digite a entrada: "))



