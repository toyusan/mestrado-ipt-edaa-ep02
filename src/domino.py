########################################################################################################################
# @file     domino.py
# @author   Airton Yassushiko Coppini Toyofuku
# @date     11/11/2021
# @brief    Classe domino, utilizada para Solução do Exercício Programa 02 da matéria Estrutura de Dados e Analise de
#           Algoritmos do curso de Mestrado em Computação Aplicada do IPT, referente ao 3° Quadrimestre de 2021:
########################################################################################################################

class Domino():

########################################################################################################################
#  @brief  Construtor da classe Domino
#  @param  esquerda: valor da esquerda do domino
#  @param  direita: valor da direita do domino
#  @retval None
    def __init__(self,esquerda,direita):
        self.esquerda = esquerda
        self.direita = direita

########################################################################################################################
#  @brief  Metodo para inverter a peça do domino [e|d] -> [d|e]
#  @param  None
#  @retval None
    def inverte(self):
        x = self.esquerda
        y = self.direita
        self.esquerda = y
        self.direita = x

########################################################################################################################
#  @brief  Metodo para sobrescrever o toString padrao da classe
#  @param  None
#  @retval None
    def __repr__(self):
        return str(self.esquerda)+ str(self.direita)

########################################################################################################################
#  @brief  Metodo de comparacao entre uma peça e outra
#  @param  None
#  @retval None
    def __eq__(self,chave):
        return self.esquerda == chave.esquerda and self.direita == chave.direita