def imprime_mat(titulo, m):
    print(titulo)
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end="  ")
        print()


def ler_matriz(titulo, m):
    print("\nForneça os dados para ", titulo)
    for i in range(len(m)):
        print(f"Dados para linha {i}:")
        for j in range(len(m[i])):
            m[i][j] = int(input(f"   {titulo}[{i}][{j}]:"))


def ler_dimensao(titulo):
    print("\nForneça os dados para", titulo)
    qtde_linhas = int(input(f"Qtde de linhas da {titulo}: "))
    qtde_colunas = int(input(f"Qtde de colunas da {titulo}: "))
    return qtde_linhas, qtde_colunas  # monta a tupla (linhas, colunas)
