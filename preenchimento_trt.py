from selenium.webdriver.common.by import By
from time import sleep
from acoes import *

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
    try:
        sleep(1)
        navegador.find_element(By.CSS_SELECTOR, 'a.botao_adicionar')
        print("aqui 1")
        janela_atual = navegador.current_window_handle
        print("aqui 2")
        clicar(navegador, By.CSS_SELECTOR, 'a.botao_adicionar')
        print("aqui 3")
        adicionar_contratante(navegador, dados)
        print("aqui 4")
        navegador.switch_to.window(janela_atual)
        print("aqui 5")
        clicar(navegador, By.ID, 'myCont0')
        print("aqui 6")
    except:
        print("erro ao achar botao adicionar")

def adicionar_contratante(navegador, dados):
    trocar_janela_ativa(navegador)
    sleep(1)
    if len(dados['cpf']) == 11:
        escrever(navegador, By.ID, 'CPF', dados['cpf'])
        selecionar_combo_box(navegador, By.ID, 'SEXO', dados['genero'])
        escrever(navegador, By.ID, 'EMAIL', dados['email'])
    else:
        selecionar_combo_box(navegador, By.ID, 'TIPO', 8)
        escrever(navegador, By.ID, 'CNPJ', dados['cpf'])
        escrever(navegador, By.ID, 'NOMEFANTASIA', dados['fantasia'])
    escrever(navegador, By.ID, 'CEP', dados['cep'])
    sleep(3)
    # if "rua" in dados['logradouro'].lower():
    #     selecionar_combo_box(navegador, By.ID, 'TIPOLOGRADOURO', 'RUA')
    # else:
    #     selecionar_combo_box(navegador, By.ID, 'TIPOLOGRADOURO', 'AVENIDA')
    # escrever(navegador, By.ID, 'LOGRADOURO', dados['logradouro'])
    escrever(navegador, By.ID, 'ENDERECO_NUMERO', dados['numero'])
    escrever(navegador, By.ID, 'COMPLEMENTO', dados['complemento'])
    # escrever(navegador, By.ID, 'BAIRRO', dados['bairro'])
    # escrever(navegador, By.ID, 'CIDADE', dados['cidade'])
    # escrever(navegador, By.ID, 'UF', dados['UF'])
    sleep(1)
    print("cheguei aqui")
    clicar(navegador, By.CSS_SELECTOR, '#cad_botoes')
    clicar(navegador, By.ID, 'save')
    print("cheguei aqui2")


def proprietario(navegador, dados):
    clicar(navegador, By.ID, 'proprietario0_AproveitaDados')
    if len(dados['cpf']) == 11:
        print("aqui 7")
        campo = navegador.find_element(By.ID, 'contratante0_CampoContratantePFNome')
        print("aqui 8")
        clicar(navegador, By.ID, 'contratante0_CampoContratantePFNome')
        print("aqui 9")
        navegador.execute_script("arguments[0].value = '';", campo)
        print("aqui 10")
        escrever(navegador, By.ID, 'contratante0_CampoContratantePFNome', dados['nome'])
        print("aqui 11")
    else:
        campo = navegador.find_element(By.ID, 'contratante0_CampoContratantePJNome')
        print("aqui 12")
        clicar(navegador, By.ID, 'contratante0_CampoContratantePJNome')
        print("aqui 13")
        navegador.execute_script("arguments[0].value = '';", campo)
        print("aqui 14")
        escrever(navegador, By.ID, 'contratante0_CampoContratantePJNome', dados['nome'])
        print("aqui 15")

    escrever(navegador, By.ID, 'CONTRATO_NUMERO', dados['numero_orcamento'])
    escrever(navegador, By.ID, 'CONTRATO_DATAINICIO0', dados['data_inicial'])
    escrever(navegador, By.ID, 'CONTRATO_DATAFIM0', dados['data_final'])
    try:
        clicar(navegador, By.CSS_SELECTOR, "#myCont0")
    except:
        print('CLICAR NA TELAAAA')
        sleep(8)
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
