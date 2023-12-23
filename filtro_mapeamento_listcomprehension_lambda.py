# copy, sorted, produtos.sort
# Exercícios
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

#importei essa lib para melhor visualização na saida
import pprint

#importei copy para utilização da deep copy conforme solicidado
import copy

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

# Exercício 1
# Aumente os preços dos produtos a seguir em 10%
# Gere novos_produtos por deep copy (cópia profunda)

novos_produtos = [
    #utilizei um novo dict p e tambem um filtro preco para aumentar em 10% o valor dos produtos
    {**p, 'preco': round(p['preco'] * 1.1, 2)}
    for p in copy.deepcopy(produtos)
]

# print(*produtos, sep='\n')
# print()
# print(*novos_produtos, sep='\n')

# EXERCICIO 2 
# Ordene os produtos por nome decrescente (do maior para menor)
# Gere produtos_ordenados_por_nome por deep copy (cópia profunda)
produtos_ordenados_por_nome = sorted(
    #utilizei sorted para deixar os elementos ordenados decrescente com reverse = TRUE
    copy.deepcopy(produtos),
    key=lambda p: p['nome'],
    reverse=True
)
# print(*produtos, sep='\n')
# print()
# print(*produtos_ordenados_por_nome, sep='\n')


# EXERCICIO 3 
# Ordene os produtos por preco crescente (do menor para maior)
# Gere produtos_ordenados_por_preco por deep copy (cópia profunda)
produtos_ordenados_por_preco = sorted(
    #aqui o mesmo esquema, utilizei expressoes lineares(lambda) 
    # para filtrar pelo preco e na ordem do sorted(CRESCENTE)
    copy.deepcopy(produtos),
    key=lambda p: p['preco']
)

# PRINTS FINAIS

print('PRODUTOS')
print(*produtos, sep='\n')
print()
print('PRODUTOS COM 10% DE AUMENTO')
print(*novos_produtos, sep='\n')
print()
print('PRODUTOS ORDENADOS PELO NOME DECRESCENTE')
print(*produtos_ordenados_por_nome, sep='\n')
print()
print('PRODUTOS ORDENADOS PELO PREÇO CRESCENTE')
print(*produtos_ordenados_por_preco, sep='\n')