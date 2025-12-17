from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import gender_api
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from scrapper_ecg import *
from preenchimento_trt import *
from config import senha_ecg, usuario_ecg, senha_sinceti, usuario_sinceti

def abrir_navegador():
    # if headless == True:
    #     options=Options()
    #     options.add_argument('--headless')
    #     options.add_argument('--width=1920')
    #     options.add_argument('--height=1080')

    navegador = webdriver.Firefox(service=Service(), options=Options())
    navegador.maximize_window()
    return navegador

def fazer_logins(navegador):
    login_sinceti(navegador, usuario_sinceti, senha_sinceti)
    login_ecg(navegador, usuario_ecg, senha_ecg)

def criar_dados(navegador, ordem_de_servico):
    numero_orcamento = ordem_de_servico[:-2]
    
    dados_obra = pegar_dados_obra(navegador, ordem_de_servico, numero_orcamento)
    dados_cliente = pegar_dados_cliente(navegador, ordem_de_servico)

    endereco = ''
    endereco_cliente = pegar_endereco_cliente(navegador, ordem_de_servico)
    enderecosExist = verEndereco(navegador, ordem_de_servico)
    if enderecosExist == True:
        endereco = pegar_endereco_extra(navegador, ordem_de_servico)
    else:
        endereco = endereco_cliente
    # endereco_folha = pegar_endereco_folha(navegador, ordem_de_servico)
    # if endereco_folha['cep'] != '':
    #     if endereco_folha['cep'] == endereco_cliente['cep']:
    #         endereco = endereco_cliente
    #     elif endereco_folha['cep'] == endereco_extra['cep']:
    #         endereco = endereco_extra
    #     else:   
    #         endereco = endereco_cliente
    # else:
    #     endereco = endereco_cliente

    area = (dados_obra['area'])+'0'
    valor = dados_obra['preco']
    cores_anodizadas = ['BRONZE1002 ANODIZADO', 'INOX JATEADO', 'NAT. FOSCO']
    processo = 'anodizada' if dados_obra['cor'] in [cores_anodizadas] else 'pintada'
    genero = gender_api.define_gender(dados_cliente['nome'])
    datahj = (datetime.today() + timedelta(days=1)).strftime('%d%m%Y')
    data_final = (datetime.today() + timedelta(days=1) + relativedelta(months=2)).strftime('%d%m%Y')
    obs = f'Envidraçamento de sacada com {dados_obra['vidro']} e esquadrias de aluminio {processo} na cor {dados_obra['cor']}.'
    dados = {
        'numero_orcamento' : numero_orcamento,
        'nome' : dados_cliente['nome'],
        'fantasia' : dados_cliente['fantasia'],
        'genero' : genero,
        'cpf' : dados_cliente['cpf'],
        'email' : dados_cliente['email'],
        'cep' : endereco['cep'],
        'numero' : endereco['numero'],
        'complemento' : endereco['complemento'],
        'telefone' : endereco['telefone'],
        'uf' : endereco['uf'],
        'cidade' : endereco['cidade'],
        'logradouro' : endereco['logradouro'],  
        'area' : area, 
        'cor' : dados_obra['cor'], 
        'vidro' : dados_obra['vidro'], 
        'preco' : valor,
        'processo' : processo,
        'observacao' : obs,
        'data_inicial' : datahj,
        'data_final' : data_final
    }
    return dados

def preencher_trts(navegador, dados):
    criar_nova_trt(navegador)
    preencher_observacao(navegador, dados)
    adicionar_atividade(navegador, dados)
    informar_contratante(navegador, dados)
    proprietario(navegador, dados)
    selecionar_coordenadas(navegador)
    validacao(navegador)
    gerar_nome_arquivo(navegador, dados)

