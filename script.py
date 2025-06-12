# from busca_dados import criar_dados
from utils import validar_ordem_de_servico

lista_de_pedidos = []

while True:
    
    ordem_de_servico = input('Digite a ordem de serviço no formato xxxx/xx-x: ').strip()
    while validar_ordem_de_servico(ordem_de_servico) != True:
        print('A ordem de serviço informada não é valida.')
        ordem_de_servico = input('Digite a ordem de serviço no formato xxxx/xx-x: ').strip()
    lista_de_pedidos.append(ordem_de_servico)
    print(f'OS {ordem_de_servico} adicionada com sucesso. Até o momento, foram adicionadas as OS {', '.join(lista_de_pedidos)}.')
    res = input('Digite a ordem de serviço da próxima TRT ou para')
# criar_dados(ordem_de_servico)

