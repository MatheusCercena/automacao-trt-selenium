from selenium.webdriver.common.by import By
from time import sleep
from acoes import *
import pyautogui

def login_sinceti(navegador, usuario, senha):
    navegador.get('https://servicos.sinceti.net.br/')
    escrever(navegador, By.ID, 'login', usuario)
    escrever(navegador, By.ID, 'senha', senha)
    clicar(navegador, By.ID, 'code')
    sleep(15)

def criar_nova_trt(navegador):
    navegador.get('https://servicos.sinceti.net.br/app/view/sight/main.php?form=CadastroART')
    selecionar_combo_box(navegador, By.ID, 'TIPOART', 'COD101')
    clicar(navegador, By.CLASS_NAME, 'ajs-ok')
    selecionar_combo_box(navegador, By.ID, 'FORMADEREGISTRO', '5')

def preencher_observacao(navegador, dados):
    selecionar_combo_box(navegador, By.ID, 'FINALIDADE', '29')
    escrever(navegador, By.ID, 'OBSERVACAO', dados['observacao'])
    selecionar_combo_box(navegador, By.ID, 'ACAOINSTITUCIONAL', '17')

def adicionar_atividade(navegador, dados):
    clicar(navegador, By.ID, 'NOVO_ATIVIDADE')
    selecionar_combo_box(navegador, By.ID, 'NIVEL0', '1004')
    selecionar_combo_box(navegador, By.ID, 'ATIVIDADEPROFISSIONAL0', '4200')
    escrever(navegador, By.ID, 'LABELATUACAO0', '1112')
    clicar(navegador, By.CSS_SELECTOR, '#listaAtividadeEscolherATUACAO0 > ul:nth-child(1) > li:nth-child(1)')
    selecionar_combo_box(navegador, By.ID, 'UNIDADE0', '2')
    escrever(navegador, By.ID, 'QUANTIDADE0', dados['area'])

def informar_contratante(navegador, dados):
    clicar(navegador, By.ID, 'NOVO_CONTRATO')
    if len(dados['cpf']) == 11:
        clicar(navegador, By.ID, 'contratante0_ContratantePFNome')
        escrever(navegador, By.ID, 'contratante0_CampoContratantePFNome', dados['nome'])
    else:
        clicar(navegador, By.ID, 'contratante0_ContratantePJNome')
        escrever(navegador, By.ID, 'contratante0_CampoContratantePJNome', dados['nome'])
    clicar(navegador, By.ID, 'myCont0')
    janela_atual = navegador.current_window_handle
    clicar(navegador, By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[3]/div/div/form/div[2]/div[4]/div[9]/div[1]/div/div[7]/div/div[4]/div[12]/div/a')
    adicionar_contratante(navegador, dados)
    navegador.switch_to.window(janela_atual)
    if len(dados['cpf']) == 11:
        campo = navegador.find_element(By.ID, 'contratante0_CampoContratantePFNome')
        clicar(navegador, By.ID, 'contratante0_CampoContratantePFNome')
        navegador.execute_script("arguments[0].value = '';", campo)
        escrever(navegador, By.ID, 'contratante0_CampoContratantePFNome', dados['nome'])
    else:
        campo = navegador.find_element(By.ID, 'contratante0_CampoContratantePJNome')
        clicar(navegador, By.ID, 'contratante0_CampoContratantePJNome')
        navegador.execute_script("arguments[0].value = '';", campo)
        escrever(navegador, By.ID, 'contratante0_CampoContratantePJNome', dados['nome'])
    clicar(navegador, By.ID, 'myCont0')

def adicionar_contratante(navegador, dados):
    sleep(1)
    trocar_janela_ativa(navegador)
    if len(dados['cpf']) == 11:
        escrever(navegador, By.ID, 'CPF', dados['cpf'])
        selecionar_combo_box(navegador, By.ID, 'SEXO', dados['genero'])
        escrever(navegador, By.ID, 'EMAIL', dados['email'])
    else:
        selecionar_combo_box(navegador, By.ID, 'TIPO', 8)
        escrever(navegador, By.ID, 'CNPJ', dados['cpf'])
        escrever(navegador, By.ID, 'NOMEFANTASIA', dados['fantasia'])
    escrever(navegador, By.ID, 'CEP', dados['cep'])
    sleep(1)
    escrever(navegador, By.ID, 'ENDERECO_NUMERO', dados['numero'])
    escrever(navegador, By.ID, 'COMPLEMENTO', dados['complemento'])
    escrever(navegador, By.ID, 'ENDERECO_TELEFONE', dados['telefone'])
    clicar(navegador, By.ID, 'save')
    sleep(1)

def proprietario(navegador, dados):
    clicar(navegador, By.ID, 'proprietario0_AproveitaDados')
    escrever(navegador, By.ID, 'CONTRATO_NUMERO', dados['numero_orcamento'])
    escrever(navegador, By.ID, 'CONTRATO_DATAINICIO0', dados['data_inicial'])
    escrever(navegador, By.ID, 'CONTRATO_DATAFIM0', dados['data_final'])
    clicar(navegador, By.CSS_SELECTOR, "div.cad_form_cont_campo:nth-child(27) > img:nth-child(3)")
    escrever(navegador, By.ID, 'CONTRATO_VALOR0', dados['preco'])
    sleep(1)
    
def selecionar_coordenadas(navegador):
    clicar(navegador, By.CSS_SELECTOR, '#evtContratoEnderecoContainerSpecific0 > div:nth-child(3) > input:nth-child(1)')
    clicar(navegador, By.ID, 'ESCOLHERCORDENADASGMAP')
    trocar_janela_ativa(navegador)
    fechar_janelas_extras(navegador)

def validacao(navegador):
    clicar(navegador, By.ID, 'code')
    res = input("Insira a validação e confira os dados, então clique enter ou 'parar': ")
    if res == 'parar':
        return False
    else:
        return True
    
def gerar_nome_arquivo(navegador, dados):
    print('Nome do boleto: ')
    print(f'Boleto_TRT_{dados['nome'].replace(' ', '')}_{dados['numero_orcamento'].replace('/', '-')}')

    # clicar(navegador, By.ID, 'emitirBoleto')
    # clicar(navegador, By.ID, 'save')

    res = input("Baixe o boleto e confira os dados, então clique enter.")
