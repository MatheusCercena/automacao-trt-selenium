from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pyautogui

def esperar_ajax(navegador):
    espera = WebDriverWait(navegador, 100)
    espera.until(EC.invisibility_of_element_located((By.ID, "ajax-overlay")))

def selecionar_combo_box(navegador, tipo_seletor, seletor, valor):
    esperar_ajax(navegador)
    objeto = navegador.find_element(tipo_seletor, seletor)
    combo_box = Select((objeto))
    combo_box.select_by_value(valor)

def clicar(navegador, tipo_seletor, seletor):
    esperar_ajax(navegador)
    espera_objeto = WebDriverWait(navegador, 100)
    espera_objeto.until(EC.element_to_be_clickable((tipo_seletor, seletor)))
    objeto = navegador.find_element(tipo_seletor, seletor)
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", objeto)
    objeto.click()

def escrever(navegador, tipo_seletor, seletor, key):
    esperar_ajax(navegador)
    espera_objeto = WebDriverWait(navegador, 100)
    espera_objeto.until(EC.element_to_be_clickable((tipo_seletor, seletor)))
    objeto = navegador.find_element(tipo_seletor, seletor)
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", objeto)
    objeto.send_keys(key)


def trocar_janela_ativa(navegador):
    janelas = navegador.window_handles
    WebDriverWait(navegador, 100).until(EC.number_of_windows_to_be(2))
    navegador.switch_to.window(janelas[1])
    WebDriverWait(navegador, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

def limpar(navegador, tipo_seletor, seletor):
    objeto = navegador.find_element(tipo_seletor, seletor)
    objeto.clear()

#CONFIG
vidro = 'incolor temperado'
processo = 'pintada'
cor_aluminio = 'branco'
obs = f'Envidraçamento de sacada com vidro liso {vidro} e esquadrias de aluminio {processo} de {cor_aluminio}.'
quantidade = int(str(10)+'000')
nome = 'Marcelo Germano'
cpf = '12345678900'
genero = 'M'
email = 'email'
cep = 12345678
numero = 1234
complemento = 'Rua Tal Tal Tal, Residencial Tal'
telefone = 48998765432
ordem_de_servico = '356/24'
datahj = '060625'
data_final = '060825'
valor = int(str(5000)+'00')

navegador = webdriver.Firefox(service=Service(), options=Options())
navegador.get('https://servicos.sinceti.net.br/')
navegador.maximize_window()

#LOGIN
escrever(navegador, By.ID, 'login', '12676911902')
escrever(navegador, By.ID, 'senha', 'mdvHxi65')
clicar(navegador, By.ID, 'code')
sleep(15)

navegador.get('https://servicos.sinceti.net.br/app/view/sight/main.php?form=CadastroART')

#SELECIONAR MODELO
selecionar_combo_box(navegador, By.ID, 'TIPOART', 'COD101')
clicar(navegador, By.CLASS_NAME, 'ajs-ok')

#FORMA DE REGISTRO
selecionar_combo_box(navegador, By.ID, 'FORMADEREGISTRO', '5')

#DADOS
selecionar_combo_box(navegador, By.ID, 'FINALIDADE', '29')
escrever(navegador, By.ID, 'OBSERVACAO', obs)

#AÇÃO INSTITUICIONAL
selecionar_combo_box(navegador, By.ID, 'ACAOINSTITUCIONAL', '17')

#ATIVIDADES CONTRATADAS
clicar(navegador, By.ID, 'NOVO_ATIVIDADE')
selecionar_combo_box(navegador, By.ID, 'NIVEL0', '1004')
selecionar_combo_box(navegador, By.ID, 'ATIVIDADEPROFISSIONAL0', '4200')
escrever(navegador, By.ID, 'LABELATUACAO0', '1112')
clicar(navegador, By.CSS_SELECTOR, '#listaAtividadeEscolherATUACAO0 > ul:nth-child(1) > li:nth-child(1)')
selecionar_combo_box(navegador, By.ID, 'UNIDADE0', '2')
escrever(navegador, By.ID, 'QUANTIDADE0', quantidade)

#CONTRATO
clicar(navegador, By.ID, 'NOVO_CONTRATO')
clicar(navegador, By.ID, 'contratante0_ContratantePFNome')
escrever(navegador, By.ID, 'contratante0_CampoContratantePFNome', nome)
clicar(navegador, By.ID, 'myCont0')
# clicar(navegador, By.CLASS_NAME, 'botao_adicionar')

# #ADICIONAR CONTRATANTE
# trocar_janela_ativa(navegador)
# escrever(navegador, By.ID, 'CPF', cpf)
# selecionar_combo_box(navegador, By.ID, 'SEXO', genero)
# escrever(navegador, By.ID, 'EMAIL', email)

# escrever(navegador, By.ID, 'CEP', cep)
# escrever(navegador, By.ID, 'ENDERECO_NUMERO', numero)
# escrever(navegador, By.ID, 'COMPLEMENTO', complemento)
# escrever(navegador, By.ID, 'ENDERECO_TELEFONE', telefone)
# # clicar(navegador, By.ID, 'save')

# janela_atual = navegador.current_window_handle
# navegador.switch_to.window(janela_atual)

# limpar(navegador, By.ID, 'contratante0_ContratantePFNome')
# clicar(navegador, By.ID, 'myCont0')
# escrever(navegador, By.ID, 'contratante0_CampoContratantePFNome', nome)

clicar(navegador, By.ID, 'proprietario0_AproveitaDados')
escrever(navegador, By.ID, 'CONTRATO_NUMERO', ordem_de_servico)
escrever(navegador, By.ID, 'CONTRATO_DATAINICIO0', datahj)
escrever(navegador, By.ID, 'CONTRATO_DATAFIM0', data_final)
escrever(navegador, By.ID, 'CONTRATO_VALOR0', valor)
pyautogui.press('enter')
clicar(navegador, By.CSS_SELECTOR, '#evtContratoEnderecoContainerSpecific0 > div:nth-child(3) > input:nth-child(1)')

trocar_janela_ativa(navegador)

navegador.close()
janela_atual = navegador.current_window_handle
navegador.switch_to.window(janela_atual)

#VALIDACAO
clicar(navegador, By.ID, 'code')
