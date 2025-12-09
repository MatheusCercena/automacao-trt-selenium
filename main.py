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
    # print('Insira abaixo as Ordens de Serviço das TRTs a serem feitas, lembrando que após abrir o navegador você terá 15 segundos para inserir a validação do login no SINCETI.')
    if res == '1': 
        lista_de_pedidos = ['2010/25-1', '2003/25-1']
        fazer_logins(navegador)
        for i, ordem_de_servico in enumerate(lista_de_pedidos):
            print(f'Faltam {i-len(lista_de_pedidos)} TRTs')
            print(f'OS: {ordem_de_servico}')
            dados = criar_dados(navegador, ordem_de_servico)
            tabela = pandas.DataFrame([dados])
            print(tabela.T)
            preencher_trts(navegador, dados)
    elif res == '2':
        fazer_logins(navegador)
        dar_baixa(navegador)

#     navegador = abrir_navegador()
#     lista_de_pedidos = ["1933/25-1", "1984/25-1", "1982/25-1", "1980/25-1", "2000/25-1", "2024/25-1", "1983/25-1", "2044/25-1", "1990/25-1", "1985/25-1", "2018/25-1", "1998/25-1", "2125/25-1", "2020/25-1", "1997/25-1"]
#     fazer_logins(navegador)

#     for i, ordem_de_servico in enumerate(lista_de_pedidos):
#         dados = criar_dados(navegador, ordem_de_servico)
#         # Formatar CPF
#         cpf_formatado = f"{dados['cpf'][:3]}.{dados['cpf'][3:6]}.{dados['cpf'][6:9]}-{dados['cpf'][9:]}"
#         # Formatar Preço (assumindo que 567000 é R$ 567.000,00)
#         preco_com_virgula = dados['preco'][:-2] + "," + dados['preco'][-2:]
#         preco_formatado = f"R$ {float(preco_com_virgula.replace(',', '.')):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
#         # Formatar Datas (assumindo formato DDMMYYYY)
#         data_inicial_formatada = f"{dados['data_inicial'][:2]}/{dados['data_inicial'][2:4]}/{dados['data_inicial'][4:]}"
#         data_final_formatada = f"{dados['data_final'][:2]}/{dados['data_final'][2:4]}/{dados['data_final'][4:]}"
#         area_string = str(dados['area'])
#         area_formatada = area_string[:-2] + "," + area_string[-2:] # Resultado: '3,65'
#         # Geração do output formatado
#         output_formatado = f"""
# ==================================================
#            DADOS DO ORÇAMENTO N° {dados['numero_orcamento']}
# ==================================================

# INFORMAÇÕES DO CLIENTE

# Nome Completo: {dados['nome']}
# Nome Fantasia: {dados['fantasia']}
# CPF: {cpf_formatado}
# Gênero: {dados['genero']}
# E-mail: {dados['email']}
# Telefone: {dados['telefone']}

# ENDEREÇO

# Logradouro: {dados['logradouro']}, {dados['numero']}
# Complemento: {dados['complemento']}
# CEP: {dados['cep']}
# Cidade/UF: {dados['cidade']}/{dados['uf']}

# DETALHES DO PROJETO

# Área (m²): {area_formatada}
# Cor da Esquadria: {dados['cor'].capitalize()}
# Especificação do Vidro: {dados['vidro'].capitalize()}

# VALOR E PRAZOS

# Preço Total: {preco_formatado}
# Data Início Prevista: {data_inicial_formatada}
# Data Fim Prevista: {data_final_formatada}

# OBSERVAÇÕES

# {dados['observacao']}
# """

#         print(output_formatado)
