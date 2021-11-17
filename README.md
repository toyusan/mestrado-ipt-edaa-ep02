# Jogo de Dominó com Lista Ligada

---

Tabela de conteúdos
=================
<!--ts-->
   * [Sobre o projeto]
   * [Funcionalidades]
   * [Como executar o projeto]
     * [Pré-requisitos]
     * [Rodando o programa]
	 * [Exemplos de testes]
   * [Autor]
   * [Licença]
<!--te-->

---

## Sobre o projeto

Solução do Exercício Programa 02 da matéria Estrutura de Dados e Analise de Algoritmos do curso de Mestrado em Computação Aplicada do IPT, referente ao 3° Quadrimestre de 2021:

>"Neste exercício programa você deverá utilizar os conhecimentos de listas ligadas aprendidos na disciplina para solução de um jogo de mesa bastante conhecido, o dominó. No jogo de dominó as peças com dois valores devem ser colocadas na mesa em sequência, de tal forma que os valores de peças imediatamente vizinhas sejam iguais. Desta forma, o propósito do seu programa é determinar se é possível colocar todas as peças de um dado conjunto em uma formação válida(...) Assim, dado um conjunto de peças de dominó, cada peça tem dois valores X e Y , com X e Y variando de 0 a 6 (X pode ser igual a Y ). Sua tarefa é implementar um programa que determine se é possível organizar todas as peças recebidas em sequência, obedecendo às regras do jogo de dominó. A entrada do programa deve ser um arquivo texto (.txt) composto de vários conjuntos de teste. A primeira linha de um conjunto de testes deve conter um número inteiro N que indica a quantidade de peças do conjunto. As N linhas seguintes contêm, cada uma, a descrição de uma peça. Uma peça é descrita por dois inteiros X e Y (0 ≤ X ≤ 6 e 0 ≤ Y ≤ 6) que representam os valores de cada lado da peça. O final da entrada é indicado por N = 0. A Figura 2 apresenta um exemplo possível de entrada para o programa. 
> 
> 3  
> 0 1  
> 2 1  
> 2 1  
> 2  
> 1 1  
> 0 0  
> 6  
> 3 0  
> 0 0  
> 1 6  
> 4 1  
> 0 6  
> 2 3  
> 0  
> 
> Para cada conjunto de teste da entrada seu programa deve produzir quatro linhas na saída. A primeira linha deve conter um identificador do conjunto de teste, no formato "Teste n", onde n é numerado a partir de 1. A segunda linha deve conter a expressão "sim" se for possível organizar todas as peças em uma formação válida ou a expressão "nao" (note a ausência de acento) caso contrário. A terceira linha deve apresentar a sequência de alocação das peças (separadas por "|", caso seja possível organizá-las ou "nao" caso contrário. A quarta linha deve ser deixada em branco." Exemplo de saída da tela:
>  
>  Teste 1  
>  sim  
>  01|12|21  
>  
>  Teste 2  
>  nao  
>  nao  
>  
>  Teste 3  
>  sim  
>  23|30|00|06|61|14  

---

## Funcionalidades

>- O usuário entra com o caminho do arquivo de teste contendo a lista de peças de dominó, conforme o enunciado;

>- O software verifica se existe uma formação para o conjunto de peças, apresentado a formação em caso positivo ou "nao" em caso negativo.
---

## Como executar o projeto

### Pré-requisitos

* [Python 3.8.7](https://www.python.org/downloads/release/python-387/);
 
#### Rodando o programa

> Colocar os três arquivos no mesmo diretório:

>- ep02.py 
>- lista_encadeada.py 
>- domino.py 
>- teste.txt

> Localizar o arquivo ep02.py e clicar duas vezes para abri-lo;

> Digitar o caminho do arquivo de testes;

> Pressionar enter para iniciar o processo de analise do arquivo. 

#### Exemplos de testes


- Conteúdo do arquivo teste.txt:

<div style="text-align: center">

3  
0 1  
2 1  
2 1  
2  
1 1  
0 0  
6  
3 0  
0 0  
1 6  
4 1  
0 6  
2 3  
2  
1 0  
1 3  
4  
5 6  
8 8  
2 1  
4 5  
8  
1 0  
2 2  
3 1  
4 5  
4 2  
5 3  
0 3  
4 4  
1  
1 2  
9  
2 2  
2 3  
3 4  
0 4  
1 0  
5 1  
1 6  
6 6  
2 6  
0  

</div>

Ao iniciar o programa, entrar com o endereço do diretório:

> Entre com o endereço do arquivo: D:\Workspace\mestrado-ipt-edaa-ep02\src
>
> Teste 1  
> sim  
> 12|21|10  
> 
> Teste 2  
> nao  
> nao  
> 
> Teste 3  
> sim  
> 41|16|60|00|03|32  
> 
> Teste 4  
> sim  
> 31|10  
> 
> Teste 5  
> nao  
> nao  
> 
> Teste 6  
> sim  
> 31|10|03|35|54|44|42|22  
> 
> Teste 7  
> nao  
> nao  
> 
> Teste 8  
> sim  
> 26|66|61|51|10|04|43|32|22  

---

### Autor 

- Airton Y. C. Toyofuku
- airton.toyofuku@gmail.com

---
### Licença
Este projeto esta sob a licença [MIT](./LICENSE).

