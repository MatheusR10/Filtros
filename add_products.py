#importei copy para utilização da deep copy conforme solicidado
import copy

#importei os para limpar o terminal evitando poluição
import os

import pprint

#criei essa função para utilizar a funcao pretty print(pprint) e padronizar ela 
def p(v):
    pprint.pprint(v, sort_dicts=False)

produtos = [
    {'nome': 'MONITOR GAMER TGT, 24 POL. VA, FHD 165HZ', 'preco': 609.99},
    {'nome': 'CADEIRA GAMER TGT HERON TX TECIDO', 'preco': 1399.90},
    {'nome': 'CAIXA DE SOM JBL AUTHENTICS 300, 50W RMS, BT', 'preco': 3099.90},
    {'nome': 'BASE PARA NOTEBOOK MANCER ALOY, RGB, ATE 17 POL', 'preco': 99.99},
    {'nome': 'CADEIRA OFFICE ZINNIA HERA', 'preco': 149.90},
]

print('ADICIONANDO PRODUTOS NA LISTA')
#EX 1##############################################################################
'''
def adicionar_produto(lista, nome, preco):
    # Cria uma deep copy da lista com os produtos antigos e o novo produto
    nova_lista = copy.deepcopy(lista)

    #adicionando novo produto na 'copia profunda' da lista
    nova_lista.append({'nome': nome, 'preco': preco})
    
    # Retorna a nova lista
    return nova_lista

while True:
    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar [c]lear [s]air: ')
    if isinstance(opcao,str):       
        if opcao == 'a' or opcao =='A':
            indice_str = input(
                'Escolha o índice para apagar: '
            )
            try:
                indice = int(indice_str)                
                del produtos[indice]
            except ValueError:
                print('Por favor digite número int.')
            except IndexError:
                print('Índice não existe na lista de produtos')
            except Exception:
                print('Erro desconhecido')
        elif opcao == 'c'or opcao =='C':
            produtos.clear()
        elif opcao == 'i'or opcao =='I':
            os.system('cls')
            nome = input('Nome do novo produto: ')
            preco = input('Valor do novo produto: ')
            produtos = adicionar_produto(produtos,nome,preco)
        elif opcao == 's'or opcao =='S':
            break
        elif opcao == 'l' or opcao =='L':
            os.system('cls')

            if len(produtos) == 0:
                print('Nada para listar')

            for i, valor in enumerate(produtos):
               print(i, valor)
    else:
        ('Por favor, escolha apenas letras.')
''' 
#FIM EX1###########################################################################

#EX 2 ##############################################################################

# Define uma função para adicionar novos atributos aos produtos
def adicionar_atributos(lista, novos_atributos):
    # Cria uma deep copy da lista com os produtos antigos
    nova_lista = copy.deepcopy(lista)

    # Usa um loop for para percorrer cada produto da lista
    for produto in nova_lista:
        # Usa outro loop for para percorrer cada novo atributo
        for atributo in novos_atributos:
            # Verifica se o produto já tem o atributo
            if atributo not in produto:
                # Se não tiver, adiciona o atributo com um valor vazio
                produto[atributo] = ""

    # Retorna a nova lista
    return nova_lista

# Lista de novos atributos
novos_atributos = ["cor", "marca", "peso"]

# Adiciona os novos atributos aos produtos
produtos = adicionar_atributos(produtos, novos_atributos)

# Imprime a nova lista de produtos
p(produtos)

#FIM EX 2 ##########################################################################

#criar funcao para adicionar elemento na lista com n atributosmigagaga