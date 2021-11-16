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
#  @brief  Faz a comparaçao entre as pecas da lista e retorna uma combinacao possivel
#  @param  lista_pecas: lista contendo as pecas de domino sem formacao
#  @param  peca: peca a ser comparada inicialmente para determinar se eh possivel uma formacao
#  @retval string contendo a formacao, caso exista
def verifica_formacao(peca, lista_pecas):

    tamanho_lista = lista_pecas.tamanho()
    proxima = lista_pecas.cabeca
    achou = 0

    # Verifica se existe uma combinacao possivel
    for i in range(0, tamanho_lista, 1):
        #print('comparando %s com %s: ' % (str(peca.dado), str(proxima.dado)))

        # Fazendo uma serie de comparacoes, considerando os dois lados da peca e fazendo as rotacoes necessarias se for preciso
        # Peca encaixa normalmente ab|bc
        if peca.dado.direita == proxima.dado.esquerda:
            achou = True
            break
        else:
            # Peca de inicio está invertida ab|ac
            if peca.dado.esquerda == proxima.dado.esquerda:
                peca.dado.inverte()
                achou = True
                break
            else:
                # Proxima peca esta invertida: ab|cb
                if peca.dado.direita == proxima.dado.direita:
                    proxima.dado.inverte()
                    achou = True
                    break
                else:
                    # As duas pecas estao invetidas ab|ca
                    if peca.dado.esquerda == proxima.dado.direita:
                        peca.dado.inverte()
                        proxima.dado.inverte()
                        achou = True
                        break
        proxima = proxima.proximo

    # Se achou algumas combinacao valida
    if achou:
        # Se so tem um peca na lista para encaixar, retonar a formacao
        if tamanho_lista == 1:
            return str(peca.dado) + "|" + str(proxima.dado)
        else:
            # Se tem mais pecas para comparar, criamos outra lista e removemos a proxima peca para chamar a recursao...
            lista_aux = lista_encadeada.ListaEncadeada()
            lista_aux = copy.deepcopy(lista_pecas)
            lista_aux.remove(proxima)

            # ... chamamos a recursao com uma peca a menos, que ja foi ordenada
            formacao = verifica_formacao(proxima,lista_aux)

            # Se a formacao retornar vazia, nao existe uma formacao valiza
            if(formacao == ''):
                return ''
            # Caso contrario, retorna a formacao + os resultados anteriores
            else:
                return str(peca.dado) + '|' + formacao

    # Nao achou nenhuma combinacao possivel, entao retorna formacao vazia
    else:
        return ''

########################################################################################################################

print("=============================================")
print("=     Jogo de Domino com Lista Ligada       =")
print("=============================================")

import copy
import domino
import lista_encadeada

address = input("Entre com o endereço do arquivo: ")
#address = "D:/Workspace/00.GitHub ToyuSan/Mestrado IPT - Estrutura de Dados e Analises de Algoritmos/mestrado-ipt-edaa-ep02/src"

# Abre o arquivo no modo leitura (r)
lines = open_file(address, 'r')

# Variáveis usadas no while para ler o arquivo e identificar qual o caso de teste
teste = 0
i = 0

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

        # Colocando os dominos na lista encadeada
        for j in range (i + 1, i + 1 + qtd_dominos, 1):
            line = lines[j]
            peca = domino.Domino(int(line[0]),int(line[2]))
            lista_pecas.insere(peca)
        #print('Lista de pecas: ' + str(lista_pecas))

        peca_atual = lista_pecas.cabeca
        # Vamos verificar se existe uma formação valida para cada peça
        for k in range(0, lista_pecas.tamanho(), 1):

            # Fazemos uma cópia da lista de dominos, removendo a peça que temos interesse em comparar
            lista_aux = lista_encadeada.ListaEncadeada()
            lista_aux = copy.deepcopy(lista_pecas)
            lista_aux.remove(peca_atual)

            # Verifica se, a partir da peca selecionada, existe uma formacao possivel
            formacao = verifica_formacao(peca_atual, lista_aux)

            # Se existe uma formacao possivel, entao paramos o laco
            if (len(formacao) > 0):
                # print('Achou %s' % str(formacao))
                break
            # Senao, tentamos outra formaçao, considerando a proxima peca da lista como ponto de inicio
            peca_atual = peca_atual.proximo

        # Apresentacao do resultado do algoritmo
        if(formacao == ''):
            print('nao\n' + 'nao')
        else:
            print('sim\n' + formacao)
        print()

    # Passando para o proximo conjunto de testes do arquivo
    i = i + qtd_dominos + 1


print("\n===========================================")

saida = input("> Precione enter para sair...")