def validar_ordem_de_servico(ordem_de_servico):
    try:
        partes1_e_2, parte3 = ordem_de_servico.split('-')
        parte1, parte2 = partes1_e_2.split('/')
        if len(parte1) > 4 or len(parte2) != 2 or len(parte3) != 1:
            return False
        parte1 = int(parte1)
        parte2 = int(parte2)
        parte3 = int(parte3)
        return True
    except:
        return False

def solicitar_ordens_de_servico():
    lista_de_pedidos = []
    while True:
        ordem_de_servico = input('Digite a ordem de serviço no formato xxxx/xx-x ou "parar" para parar: ').strip()
        if ordem_de_servico == 'parar':
            break
        while validar_ordem_de_servico(ordem_de_servico) != True:
            print('A ordem de serviço informada não é valida.')
            ordem_de_servico = input('Digite a ordem de serviço no formato xxxx/xx-x: ').strip()
            if ordem_de_servico == 'parar':
                break
        lista_de_pedidos.append(ordem_de_servico)
        print(f'OS {ordem_de_servico} adicionada com sucesso. Até o momento, foram adicionadas as OS {', '.join(lista_de_pedidos)}.')
    return lista_de_pedidos

