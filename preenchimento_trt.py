from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from time import sleep
import pyautogui
from acoes import *

navegador = webdriver.Firefox(service=Service(), options=Options())

def login_sinceti(usuario, senha):
    navegador.get('https://servicos.sinceti.net.br/')
    navegador.maximize_window()
    escrever(navegador, By.ID, 'login', usuario)
    escrever(navegador, By.ID, 'senha', senha)
    clicar(navegador, By.ID, 'code')
    sleep(10)

def criar_nova_trt():
    navegador.get('https://servicos.sinceti.net.br/app/view/sight/main.php?form=CadastroART')
    selecionar_combo_box(navegador, By.ID, 'TIPOART', 'COD101')
    clicar(navegador, By.CLASS_NAME, 'ajs-ok')
    selecionar_combo_box(navegador, By.ID, 'FORMADEREGISTRO', '5')

def preencher_dados(dados):
    selecionar_combo_box(navegador, By.ID, 'FINALIDADE', '29')
    escrever(navegador, By.ID, 'OBSERVACAO', dados['observacao'])
    selecionar_combo_box(navegador, By.ID, 'ACAOINSTITUCIONAL', '17')

def adicionar_atividade(dados):
    clicar(navegador, By.ID, 'NOVO_ATIVIDADE')
    selecionar_combo_box(navegador, By.ID, 'NIVEL0', '1004')
    selecionar_combo_box(navegador, By.ID, 'ATIVIDADEPROFISSIONAL0', '4200')
    escrever(navegador, By.ID, 'LABELATUACAO0', '1112')
    clicar(navegador, By.CSS_SELECTOR, '#listaAtividadeEscolherATUACAO0 > ul:nth-child(1) > li:nth-child(1)')
    selecionar_combo_box(navegador, By.ID, 'UNIDADE0', '2')
    escrever(navegador, By.ID, 'QUANTIDADE0', dados['area'])

def informar_contratante(dados):
    clicar(navegador, By.ID, 'NOVO_CONTRATO')
    clicar(navegador, By.ID, 'contratante0_ContratantePFNome')
    escrever(navegador, By.ID, 'contratante0_CampoContratantePFNome', dados['nome'])
    clicar(navegador, By.ID, 'myCont0')
    # clicar(navegador, By.CLASS_NAME, 'botao_adicionar')

def adicionar_contratante(dados):
    trocar_janela_ativa(navegador)
    escrever(navegador, By.ID, 'CPF', dados['cpf'])
    selecionar_combo_box(navegador, By.ID, 'SEXO', dados['genero'])
    escrever(navegador, By.ID, 'EMAIL', dados['email'])

    escrever(navegador, By.ID, 'CEP', dados['cep'])
    escrever(navegador, By.ID, 'ENDERECO_NUMERO', dados['numero'])
    escrever(navegador, By.ID, 'COMPLEMENTO', dados['complemento'])
    escrever(navegador, By.ID, 'ENDERECO_TELEFONE', dados['telefone'])
    # clicar(navegador, By.ID, 'save')

    janela_atual = navegador.current_window_handle
    navegador.switch_to.window(janela_atual)

    limpar(navegador, By.ID, 'contratante0_ContratantePFNome')
    clicar(navegador, By.ID, 'myCont0')
    escrever(navegador, By.ID, 'contratante0_CampoContratantePFNome', dados['nome'])

def contratante(dados):
    clicar(navegador, By.ID, 'proprietario0_AproveitaDados')
    escrever(navegador, By.ID, 'CONTRATO_NUMERO', dados['ordem_de_servico'])
    escrever(navegador, By.ID, 'CONTRATO_DATAINICIO0', dados['datahj'])
    escrever(navegador, By.ID, 'CONTRATO_DATAFIM0', dados['data_final'])
    pyautogui.press('enter')
    sleep(1)
    escrever(navegador, By.ID, 'CONTRATO_VALOR0', dados['valor'])
    
    
def selecionar_coordenadas():
    clicar(navegador, By.CSS_SELECTOR, '#evtContratoEnderecoContainerSpecific0 > div:nth-child(3) > input:nth-child(1)')
    clicar(navegador, By.ID, 'ESCOLHERCORDENADASGMAP')
    trocar_janela_ativa(navegador)
    fechar_janelas_extras(navegador)

def validacao():
    clicar(navegador, By.ID, 'code')