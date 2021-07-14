'''
Construir um algoritmo que contenha 3 listas:
•  Nomes de produtos
•  Preços de cada produto
•  Quantidades de cada produto
Construir uma função para imprimir um dos produtos da lista e uma função para retirar um dos produtos das listas

Forma de entrega desta atividade: Crie um repositório remoto Git no GitHub, GitLab ou Bitbucket e poste aqui apenas o link do repositório que contém o código que você desenvolveu.
'''

lst_produto = []
lst_preco  = []
lst_quantidade = []


class Produto: 
    def __init__(self, produto, preco, quantidade): 
        self.produto = produto 
        self.preco = preco 
        self.quantidade = quantidade
    
    def imprimir(self): 
        print(f'Produto: {self.produto}\nPreço: {self.preco}\nQuantidade: {self.quantidade}')
    
    
    def remover(self): 
        remover = input('Qual produto deseja remover?') 
        if remover == self.produto: 
            lst_produto.remove(self.produto)
            print('Produto removido')


a1 = Produto('Coca-Cola', 10, 15)
a1.imprimir()
'''print(f'Produto: {a1.produto}\nPreço: {a1.preco}\nQuantidade: {a1.quantidade}')'''


lst_produto.append(a1.produto) 
lst_preco.append(a1.preco)
lst_quantidade.append(a1.quantidade)

print(lst_produto)
print(lst_preco)
print(lst_quantidade)

a1.remover()
print(lst_produto)

