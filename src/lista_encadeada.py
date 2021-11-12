########################################################################################################################
# @file     lista_encadeada.py
# @author   Airton Yassushiko Coppini Toyofuku
# @date     11/11/2021
# @brief    Classes de lista encadeada e de seus Nodes, utilizada para Solução do Exercício Programa 02 da matéria
#           Estrutura de Dados e Analise de Algoritmos do curso de Mestrado em Computação Aplicada do IPT,
#           referente ao 3° Quadrimestre de 2021:
########################################################################################################################

class Node:

########################################################################################################################
#  @brief  Construtor da classe Node, que irá representar um nó da lista
#  @param  dado: valor do dado a ser armazenado
#  @param  proximo_no: ponteiro para o proximo nó da lista
#  @retval None
    def __init__(self, dado = 0, proximo = None):
        self.dado = dado
        self.proximo = proximo

    def getDado(self):
        return self.dado

    def getProximo(self):
        return  self.proximo

    def setDado(self,novo_dado):
        self.dado = novo_dado

    def setProximo(self, novo_proximo):
        self.proximo = novo_proximo

########################################################################################################################
#  @brief  Metodo para sobrescrever o toString padrao da classe
#  @param  None
#  @retval None
    def __repr__(self):
        if(self.proximo == None):
            return str(self.dado)
        else:
            return '%s|%s' % (self.dado, self.proximo)

########################################################################################################################

class ListaEncadeada:

########################################################################################################################
#  @brief  Construtor da classe ListaEncadeada com Cabeça
#  @param  None
#  @retval None
    def __init__(self):
        self.cabeca = None

########################################################################################################################
#  @brief  Metodo para sobrescrever o toString padrao da classe
#  @param  None
#  @retval None
    def __repr__(self):
        return  str(self.cabeca)

########################################################################################################################
#  @brief  Insere um dado na lista
#  @param  lista: lista encadeada em que sera inserido o dado
#  @param  dado: dado a ser inserido na lista encadeada
#  @retval None
    def insere(self,dado):
        x = Node(dado)
        x.proximo = self.cabeca
        self.cabeca = x

    def busca(self, chave):
        p = self.cabeca
        found = False
        while(p != None and not found):
            if (p.dado == chave):
                found = True
            else:
                p = p.proximo
        return found

    def tamanho(self):
        p = self.cabeca
        contador = 0
        while p != None:
            contador = contador + 1
            p = p.proximo

        return contador