from pipelines import fazer_logins, abrir_navegador, criar_dados, preencher_trts
from inputs import solicitar_ordens_de_servico
import pandas
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
    fazer_logins(navegador)

    print('Insira abaixo as Ordens de Serviço das TRTs a serem feitas, lembrando que após abrir o navegador você terá 15 segundos para inserir a validação do login no SINCETI.')
    for ordem_de_servico in lista_de_pedidos:
        dados = criar_dados(navegador, ordem_de_servico)
        tabela = pandas.DataFrame([dados])
        print(tabela.T)
        preencher_trts(navegador, dados)
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

