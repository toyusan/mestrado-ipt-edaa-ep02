########################################################################################################################
# @file     ep02.py
# @author   Airton Yassushiko Coppini Toyofuku
# @date     04/11/2021
# @brief    Solução do Exercício Programa 02 da matéria Estrutura de Dados e Analise de Algoritmos do curso de Mestrado
#           em Computação Aplicada do IPT, referente ao 3° Quadrimestre de 2021:
########################################################################################################################

########################################################################################################################
# "Neste exercício programa você deverá utilizar os conhecimentos de listas ligadas
# aprendidos na disciplina para solução de um jogo de mesa bastante conhecido, o dominó. 
# No jogo de dominó as peças com dois valores devem ser colocadas na mesa em
# sequência, de tal forma que os valores de peças imediatamente vizinhas sejam iguais.
# Desta forma, o propósito do seu programa é determinar se é possível colocar todas as
# peças de um dado conjunto em uma formação válida(...)
# Assim, dado um conjunto de peças de dominó, cada peça tem dois valores X e
# Y , com X e Y variando de 0 a 6 (X pode ser igual a Y ). Sua tarefa é implementar
# um programa que determine se é possível organizar todas as peças recebidas em
# sequência, obedecendo às regras do jogo de dominó.
# A entrada do programa deve ser um arquivo texto (.txt) composto de vários
# conjuntos de teste. A primeira linha de um conjunto de testes deve conter um número
# inteiro N que indica a quantidade de peças do conjunto. As N linhas seguintes
# contêm, cada uma, a descrição de uma peça. Uma peça é descrita por dois inteiros
# X e Y (0 ≤ X ≤ 6 e 0 ≤ Y ≤ 6) que representam os valores de cada lado da peça.
# O final da entrada é indicado por N = 0. A Figura 2 apresenta um exemplo possível
# de entrada para o programa.
# Para cada conjunto de teste da entrada seu programa deve produzir quatro linhas
# na saída. A primeira linha deve conter um identificador do conjunto de teste,
# no formato "Teste n", onde n é numerado a partir de 1. A segunda linha deve
# conter a expressão "sim" se for possível organizar todas as peças em uma formação
# válida ou a expressão "nao" (note a ausência de acento) caso contrário. A terceira
# linha deve apresentar a sequência de alocação das peças (separadas por "|", caso seja
# possível organizá-las ou "nao" caso contrário. A quarta linha deve ser deixada em
# branco."
########################################################################################################################

########################################################################################################################
#  @brief  Abre o arquivo de teste e retorna as linhas lidas em uma lista
#  @param  address: endereco do arquivo
#  @param  mode: modo e abertura do arquivo
#  @retval linhas lidas do arquivo
def open_file(address, mode):
    file = address + '/teste.txt'
    try:
        file_open = open(file, mode)
        lines = file_open.readlines()
    except:
        print("Erro ao abrir o arquivo")
    finally:
        file_open.close()
    return lines

########################################################################################################################
#  @brief  Verifica se os itens da lista satisfazem a formacao do domino
#  @param  lista: lista contendo as pecas de domino sem formacao
#  @retval None
def verifica_formacao(lista):

    print(lista)

    tamanho_lista = lista.tamanho()
    if(tamanho_lista >= 2):
        atual = lista.cabeca.dado
        proxima = lista.cabeca.proximo.dado



########################################################################################################################
print("=============================================")
print("=     Jogo de Domino com Lista Ligada       =")
print("=============================================")

import domino
import lista_encadeada

teste = 0
i = 0

#address = input("Entre com o endereço do arquivo: ")
address = "D:/Workspace/00.GitHub ToyuSan/Mestrado IPT - Estrutura de Dados e Analises de Algoritmos/mestrado-ipt-edaa-ep02/src"

# Abre o arquivo no modo leitura (r)
lines = open_file(address, 'r')

# Tratando as linhas do arquivo
while(i < len(lines)):

    # Lendo uma linha da lista de linhas
    line = lines[i]

    # verificando se não é o fim do arquivo
    if (int(line) > 0):
        # O caso de teste indica quantos dominos teremos no teste
        qtd_dominos = int(line)

        # Indicando qual teste está sendo realizado
        teste = teste + 1
        print('Teste ' + str(teste))

        # Criando uma lista encadeada
        lista_pecas = lista_encadeada.ListaEncadeada()

        # Colocando os dominos na lista ligada
        for j in range (i + 1, i + 1 + qtd_dominos, 1):
            line = lines[j]
            peca = domino.Domino(int(line[0]),int(line[2]))
            lista_pecas.insere(peca)
            #lista_encadeada.insere(lista_pecas,peca)

        # Verificando se as peças satisafazem uma formação
        verifica_formacao(lista_pecas)

    # A proxima linha de teste vai ser a quantidade de dominos lidos + 1
    i = i + qtd_dominos + 1

print("\n===========================================")

#saida = input("> Precione enter para sair...")