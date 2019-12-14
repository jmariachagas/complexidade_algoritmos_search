import numpy as np
import timeit
import random

A = []
V = []

item = 0

def embaralha_vetor(A):
    A = random.shuffle(A)
    return A

def sorteio_numero():
    item = random.choice(A)
    return item

def pesquisa_binaria(A, item):

    esquerda = 0
    direita = len(A) -1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2

        if A[meio] == item:
            return meio
        elif A[meio] > item:
            direita = meio - 1
        else:
            esquerda = meio + 1
    return -1

def ordena_vetor(A):
    A = sorted(A)
    return A


num = 1000

while(num != 0):
    A = np.arange(0, num, 1)
    for z in range(0,5):
        total = 0
        total_sorted = 0
        for x in range(0,1000):
            embaralha_vetor(A)
            #print "Vetor desordenado", A, "\n"
            item = sorteio_numero()
            A = ordena_vetor(A)
            timeit.default_timer
            total_sorted += timeit.timeit("ordena_vetor(A)", "from __main__ import ordena_vetor, A", number=1)
            #print "vetor ordenado", A
            total += timeit.timeit("pesquisa_binaria(A, item)", "from __main__ import pesquisa_binaria, ordena_vetor, A, item", number=1)
            #total = total // 1000
        total = total_sorted + total
        V.append(total)
    if num == 1000:
        arquivo = open("arquivo_pb_1000.txt", "a")
        for y in range(0, 5):
            arquivo.write(str(V[y]) + '\n')
        V = []
    elif num == 4000:
        arquivo = open("arquivo_pb_4000.txt", "a")
        for y in range(0, 5):
            arquivo.write(str(V[y]) + '\n')
        V = []
    elif num == 5000:
        arquivo = open("arquivo_pb_5000.txt", "a")
        for y in range(0, 5):
            arquivo.write(str(V[y]) + '\n')
        V = []
    elif num == 6000:
        arquivo = open("arquivo_pb_6000.txt", "a")
        for y in range(0, 5):
            arquivo.write(str(V[y]) + '\n')
        V = []
    elif num == 10000:
        arquivo = open("arquivo_pb_10000.txt", "a")
        for y in range(0, 5):
            arquivo.write(str(V[y]) + '\n')
        V = []
    num = int(input("Digite a entrada: "))

