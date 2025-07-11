from pipelines import *
from inputs import solicitar_ordens_de_servico

if __name__ == "__main__":
    lista_de_pedidos = solicitar_ordens_de_servico()
    navegador = abrir_navegador()
    fazer_logins(navegador)
    for ordem_de_servico in lista_de_pedidos:
        print('Insira abaixo as Ordens de Serviço das TRTs a serem feitas, lembrando que após abrir o navegador você terá 15 segundos para inserir a validação do login no SINCETI.')
        dados = criar_dados(navegador, ordem_de_servico)
        print(f' Dados da OS ({ordem_de_servico}): {dados}')
        preencher_trts(navegador, dados)

