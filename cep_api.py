import requests
import pandas

def busca_cep(uf, cidade, logradouro):
    link = f'https://viacep.com.br/ws/{uf}/{cidade}/{logradouro}/json/'
    requisicao = requests.get(link)
    dicionario_ceps = requisicao.json()
    tabela = pandas.DataFrame(dicionario_ceps)
    print(tabela)

def validar_cep(cep):
    link = f'https://viacep.com.br/ws/{cep}/json/'
    requisicao = requests.get(link)
    if requisicao.status_code != 200 or requisicao.text.strip() == "":
        return False
    else:
        return True
