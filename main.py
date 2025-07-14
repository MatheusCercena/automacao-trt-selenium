from pipelines import fazer_logins, abrir_navegador, criar_dados, preencher_trts
from inputs import solicitar_ordens_de_servico
import pandas

if __name__ == "__main__":
    lista_de_pedidos = solicitar_ordens_de_servico()
    navegador = abrir_navegador()
    fazer_logins(navegador)

    print('Insira abaixo as Ordens de Serviço das TRTs a serem feitas, lembrando que após abrir o navegador você terá 15 segundos para inserir a validação do login no SINCETI.')
    for ordem_de_servico in lista_de_pedidos:
        dados = criar_dados(navegador, ordem_de_servico)
        tabela = pandas.DataFrame([dados])
        print(tabela.T)
        preencher_trts(navegador, dados)

