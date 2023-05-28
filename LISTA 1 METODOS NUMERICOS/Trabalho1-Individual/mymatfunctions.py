import numpy as np
import math


def cria_mat(qtde_linhas, qtde_colunas, valor=0):
    m = qtde_linhas * [0]
    for i in range(qtde_linhas):
        m[i] = qtde_colunas * [valor]
    return m


def multiplica_matriz(ma, mb):
    linhas_mr = len(ma)
    colunas_mr = len(mb[0])
    mr = cria_mat(linhas_mr, colunas_mr)
    for i in range(linhas_mr):
        for j in range(colunas_mr):
            for k in range(len(mb)):
                mr[i][j] = mr[i][j] + ma[i][k] * mb[k][j]
    return mr

def multiplica_matriz_numpy(ma, mb):
    linhas_mr = len(ma)
    colunas_mr = len(mb[0])
    mr = cria_mat(linhas_mr, colunas_mr)
    mr= np.dot(ma,mb)
    print("Resultado da multiplicaçã ovia numpy:", mr)
    
def multiplica_escalar(me, e):
    linhas_me = len(me)
    colunas_me = len(me[0])

    for i in range(linhas_me):
        for j in range(colunas_me):
            me[i][j] = me[i][j] * e
    return me

def multiplicacao_escalar_numpy(me,e):
    linhas_me = len(me)
    colunas_me = len(me[0])
    rese = (np.multiply(me, e))/e
    print("Resultado Matriz x escalar via numpy", rese)
    print("--------------------------------")

def maior_valor(mf):
    linhas_mf = len(mf)
    colunas_mf = len(mf[0])

    for i in range(linhas_mf):
        for j in range(colunas_mf):
            if(i == 0 & j == 0):
                maior = mf[0][0]

            if(mf[i][j] > maior):
                maior = mf[i][j]

    print("O maior número é: ", maior)


def menor_valor(mf):
    linhas_mf = len(mf)
    colunas_mf = len(mf[0])

    for i in range(linhas_mf):
        for j in range(colunas_mf):
            if(i == 0 & j == 0):
                menor = mf[0][0]

            if(mf[i][j] < menor):
                menor = mf[i][j]

    print("O menor número é: ", menor)


def soma_elementos(mf):
    linhas_mf = len(mf)
    colunas_mf = len(mf[0])
    soma = 0

    for i in range(linhas_mf):
        for j in range(colunas_mf):
            soma = soma + mf[i][j]

    print("A soma dos elementos da matriz é: ", soma)


def maior_numpy(mf):

    mnp = np.array(mf)
    print("Maior valor da matriz: ", mnp.max())  # maior valor


def menor_numpy(mf):

    mnp = np.array(mf)
    print("Menor valor da matriz: ", mnp.min())  # menor valor


def soma_numpy(mf):

    mnp = np.array(mf)
    print("Somas valores da matriz: ", mnp.sum())  # soma valores


def transposta_numpy(mf):
    linhas_mf = len(mf)
    colunas_mf = len(mf[0])

    print(np.transpose(mf))


def transposta_func(mf):
    linhas_mf = len(mf)
    colunas_mf = len(mf[0])
    print(
        list(map(lambda *linhas_mf: [colunas_mf for colunas_mf in linhas_mf], *mf)))


def determinante_laplace(m_laplace):
    linhas_mf = len(m_laplace)
    colunas_mf = len(m_laplace[0])
    aux= [[0,0,0], [0,0,0], [0,0,0]]
    for i in range(len(m_laplace) - 1):               
        for j in range(len(m_laplace) - 1):
            aux[i][j] = m_laplace[(i + 1) % (len(m_laplace))][(j + 1) % (len(m_laplace))]
    resultado = regra_sarrus(aux)
    return resultado

def det_numpy(mf):
    print("Determinante: ", np.linalg.det(mf))


def regra_sarrus(m_sarrus):
    positivo = 0
    negativo = 0
    soma = 0
    for j in range(len(m_sarrus)):
        positivo = positivo + (m_sarrus[0][j] * m_sarrus[(1)][(j+1) %
                               (len(m_sarrus))] * m_sarrus[(2)][(j+2) % (len(m_sarrus))])
        negativo = negativo + (m_sarrus[2][j] * m_sarrus[(1)][(j+1) %
                               (len(m_sarrus))] * m_sarrus[(0)][(j+2) % (len(m_sarrus))])
        soma = positivo - negativo
    return soma

