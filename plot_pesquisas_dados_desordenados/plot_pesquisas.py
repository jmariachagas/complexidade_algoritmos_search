# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as opt

#valores de n
n = [1000, 4000, 5000, 6000, 10000]
#variavel de tempo de execução
tempos = []
#array com nome dos arquivos
nome_arquivos = ["pb", "pl"]

#define a função da pesquisa linear
def funcao_linear(x, a, b):
    return (a*x) + b

#define a função da pesquisa binária
def funcao_logaritimica(x, a):
    return ((np.log(x)) + (x*(np.log(x))))*a

#realiza o procedimento para todos arquivos
for nome_arquivo in nome_arquivos:
    #inicializa as variaveis de dados, medias e desvios
    dados = {}
    medias = range(len(n))
    desvios = range(len(n))
    i = 0
    for n_x in n:
        arquivo = "arquivo_%s_%04d.txt"%(nome_arquivo, n_x)
        print "carregando arquivo: %s " % arquivo
        dados[n_x] = np.loadtxt(fname=arquivo)  # carrega dados
        print "dados: %s" % dados[n_x]  # mostra dados carregados
        medias[i] = np.average(dados[n_x])  # calcula media
        desvios[i] = np.std(a=dados[n_x], ddof=False)  # ddof=calcula desvio padrao de uma amostra?
        i += 1
        print medias, desvios
    # realiza aproximacao

    if nome_arquivo == "pb":
        parametros, pcov = opt.curve_fit(funcao_logaritimica, xdata=n, ydata=medias)
        aproximados = [funcao_logaritimica(x, *parametros) for x in n]
        print "aproximados: ", aproximados
        print "parametros_otimizados:", parametros
        print "pcov:", pcov

        # usa resultados da aproximacao para plotar
        print "Tamanho de N\tMedia\t\tDesvio\t\tAproximado"
        for i in range(len(n)):
            print "%03d\t%02f\t%02f\t%02f" % (n[i], medias[i], desvios[i], aproximados[i])
        print ""
        # plota aproximação
        curva = (u"Aproximado_Pesquisa Binária")
        plt.plot(n, aproximados, label=curva, color='g')

        # plota medicoes
        curva = (u"Medido_Pesquisa Binária")
        plt.errorbar(x=n, y=medias, yerr=desvios, label=curva, linewidth=2, linestyle="", marker="o", color='g')

    else:
        parametros, pcov = opt.curve_fit(funcao_linear, xdata=n, ydata=medias)
        aproximados = [funcao_linear(x, *parametros) for x in n]
        print "aproximados: ", aproximados
        print "parametros_otimizados:", parametros
        print "pcov:", pcov

        # usa resultados da aproximacao para plotar
        print "Atraso\tMedia\t\tDesvio\t\tAproximado"
        for i in range(len(n)):
            print "%03d\t%02f\t%02f\t%02f" % (n[i], medias[i], desvios[i], aproximados[i])
        print ""
        # plota aproximação
        curva = "Aproximado_Pesquisa Linear"
        plt.plot(n, aproximados, label=curva)

        # plota medicoes
        curva = "Medido_Pesquisa Linear"
        plt.errorbar(x=n, y=medias, yerr=desvios, label=curva, linewidth=2, linestyle="", marker="o", color='b')

plt.xticks(n, [str(i) for i in n])
plt.legend(loc='best')
plt.title(u"Avaliação das Pesquisas Binária e Linear - Dados desordenados")
plt.xlabel(u"Tamanho de N")
plt.ylabel(u"Tempo de execução (s)")
plt.show()