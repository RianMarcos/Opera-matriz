from mymatfunctions import *
from mymatutils import *
import numpy as np


def multiplicacao_matrizes():
    # desempacotou a tupla, respectivamente em uma dupla atribuição
    m, n = ler_dimensao("Matriz A")
    o, p = ler_dimensao("Matriz B")
    if n == o:  # verificar se pode multiplicar
        # criação das matrizes
        ma = cria_mat(m, n)
        ler_matriz("Matriz A", ma)
        mb = cria_mat(o, p)
        ler_matriz("Matriz B", mb)

        mres = multiplica_matriz(ma, mb)
        imprime_mat("Matriz A", ma)
        imprime_mat("Matriz B", mb)
        imprime_mat("Matriz R = A * B", mres)
        print("--------------------------------")
        print("RESULTADO VIA NUMPY:")
        multiplica_matriz_numpy(ma, mb)
        print("--------------------------------")
    else:
        print(
            f"Coluna de A {n} é diferente da linha de B {o}. Não posso multiplicar!")
        print("--------------------------------")


def multiplicacao_escalar():
    # desempacotou a tupla, respectivamente em uma dupla atribuição
    m, n = ler_dimensao("Matriz E")
    # criação das matrizes
    me = cria_mat(m, n)
    ler_matriz("Matriz E", me)
    imprime_mat("Matriz E", me)
    me2 = me
    e = int(input("Informe o valor do escalar a ser multiplicado: "))
    rese = multiplica_escalar(me, e)
    imprime_mat("Resultado da matriz * escalar: ", rese)
    print("--------------------------------")
    print("Resultado via numpy:")
    multiplicacao_escalar_numpy(me,e)
    


def maior_menor_soma():
    # desempacotou a tupla, respectivamente em uma dupla atribuição
    m, n = ler_dimensao("Matriz E")
    # criação das matrizes
    mf = cria_mat(m, n)
    ler_matriz("Matriz E", mf)
    imprime_mat("Matriz E", mf)

    print("----------------------------------------")
    maior_valor(mf)

    print("----------------------------------------")
    menor_valor(mf)

    print("----------------------------------------")
    soma_elementos(mf)

    print("----------------VIA NUMPY------------------")

   # print("Maior via numpy")
    maior_numpy(mf)

    print("----------------------------------------")

    #print("Menor via numpy")
    menor_numpy(mf)

    print("----------------------------------------")
   # print("Soma via numpy")
    soma_numpy(mf)


def det_laplace():

    m, n = ler_dimensao("Matriz E")
    # criação das matrizes
    mf = cria_mat(m, n)
    ler_matriz("Matriz E", mf)
    imprime_mat("Matriz E", mf)
    print("DETERMINANTE: ", determinante_laplace(mf))
    
def det_sarrus():
    m, n = ler_dimensao("Matriz E")
    # criação das matrizes
    mf = cria_mat(m, n)
    ler_matriz("Matriz E", mf)
    imprime_mat("Matriz E", mf)

    print("O determinante sarrus via python normal é: ")
    print(regra_sarrus(mf))
    print("----------------VIA NUMPY------------------")
    det_numpy(mf)


def transposta():
    m, n = ler_dimensao("Matriz E")
    # criação das matrizes
    mf = cria_mat(m, n)
    ler_matriz("Matriz E", mf)
    imprime_mat("Matriz E", mf)

    transposta_func(mf)
    print("----------------NUMPY----------------")
    transposta_numpy(mf)


# vem a main da "aplicação"
# menu
opcao = 1
while opcao != 0:
    print("Menu de opcoes:")
    print("  0 - sair")
    print("  1 - multiplicar matrizes")
    print("  2 - multiplicar matriz por escalar")
    print("  3 - Maior, menor e soma dos elementos da matriz")
    print("  4 - determinante matriz 3x3 (Regra de Sarrus)")
    print("  5 - determinante matriz 4x4 (Teorema de Laplace)")
    print("  6 - transposta de matriz")
    opcao = int(input("  Qual sua opcao: "))
    if opcao == 1:
        print("Escolheu multipicação de matrizes ")
        multiplicacao_matrizes()
        
    elif opcao == 2:
        print("Escolheu multipicação por escalar ")
        multiplicacao_escalar()

    elif opcao == 3:
        print("Escolheu maior, menor e soma dos elemento da matriz")
        print("maior valor da matriz: ")
        maior_menor_soma()

    elif opcao == 4:
        print("Escolheu determinante matriz 3x3 regra sarrus")
        det_sarrus()
   
    elif opcao == 5:
        print("Escolheu determinante matriz 4x4 teorema de laplace")
        det_laplace()
    elif opcao == 6:
        print("Escolheu transposta de matriz")
        transposta()
    elif opcao == 0:
        print("Escolheu sair")

        # segue com as diversar opções solicitas
        # os algoritmos, sem interação com usuário, devem virar funções no módulo mymatfunctions
        # eventuais funções reutilizáveis com alguma interação deverm ser incluídos em mymatutils
        # o corpo da função escolhida deve vir neste script
        # (ver como foi distribuída a multiplicação de matrizes)
