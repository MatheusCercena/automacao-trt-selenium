from pipelines import *
from inputs import solicitar_ordens_de_servico
from dar_baixa import dar_baixa

if __name__ == "__main__":
    res = ''
    valores_res = ['1', '2']
    while res not in valores_res:
        res = input('''
O que deseja fazer? 
[1] Cadastrar novas TRTs.
[2] Dar baixa nas TRTs
Opção: ''')
    navegador = abrir_navegador()
    if res == '1': 
        lista_de_pedidos = solicitar_ordens_de_servico()
        fazer_logins(navegador)
        for ordem_de_servico in lista_de_pedidos:
            dados = criar_dados(navegador, ordem_de_servico)
            print(f' Dados da OS ({ordem_de_servico}): {dados}')
            preencher_trts(navegador, dados)
    elif res == '2': 
        fazer_logins(navegador)
        dar_baixa(navegador)

