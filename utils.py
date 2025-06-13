def validar_ordem_de_servico(ordem_de_servico):
    try:
        partes1_e_2, parte3 = ordem_de_servico.split('-')
        parte1, parte2 = partes1_e_2.split('/')
        parte1 = int(parte1)
        parte2 = int(parte2)
        parte3 = int(parte3)
        return True
    except:
        return False
    