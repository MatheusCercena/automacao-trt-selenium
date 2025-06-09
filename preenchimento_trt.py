from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By

from time import sleep
import pyautogui
import config
from acoes import *

navegador = webdriver.Firefox(service=Service(), options=Options())
navegador.get('https://servicos.sinceti.net.br/')
navegador.maximize_window()

#LOGIN
escrever(navegador, By.ID, 'login', config.usuario_sinceti)
escrever(navegador, By.ID, 'senha', config.senha_sinceti)
clicar(navegador, By.ID, 'code')
sleep(10)

navegador.get('https://servicos.sinceti.net.br/app/view/sight/main.php?form=CadastroART')

#SELECIONAR MODELO
selecionar_combo_box(navegador, By.ID, 'TIPOART', 'COD101')
clicar(navegador, By.CLASS_NAME, 'ajs-ok')

#FORMA DE REGISTRO
selecionar_combo_box(navegador, By.ID, 'FORMADEREGISTRO', '5')

#DADOS
selecionar_combo_box(navegador, By.ID, 'FINALIDADE', '29')
escrever(navegador, By.ID, 'OBSERVACAO', config.obs)

#AÇÃO INSTITUICIONAL
selecionar_combo_box(navegador, By.ID, 'ACAOINSTITUCIONAL', '17')

#ATIVIDADES CONTRATADAS
clicar(navegador, By.ID, 'NOVO_ATIVIDADE')
selecionar_combo_box(navegador, By.ID, 'NIVEL0', '1004')
selecionar_combo_box(navegador, By.ID, 'ATIVIDADEPROFISSIONAL0', '4200')
escrever(navegador, By.ID, 'LABELATUACAO0', '1112')
clicar(navegador, By.CSS_SELECTOR, '#listaAtividadeEscolherATUACAO0 > ul:nth-child(1) > li:nth-child(1)')
selecionar_combo_box(navegador, By.ID, 'UNIDADE0', '2')
escrever(navegador, By.ID, 'QUANTIDADE0', config.area)

#CONTRATO
clicar(navegador, By.ID, 'NOVO_CONTRATO')
clicar(navegador, By.ID, 'contratante0_ContratantePFNome')
escrever(navegador, By.ID, 'contratante0_CampoContratantePFNome', config.nome)
clicar(navegador, By.ID, 'myCont0')
# clicar(navegador, By.CLASS_NAME, 'botao_adicionar')

# #ADICIONAR CONTRATANTE
# trocar_janela_ativa(navegador)
# escrever(navegador, By.ID, 'CPF', config.cpf)
# selecionar_combo_box(navegador, By.ID, 'SEXO', config.genero)
# escrever(navegador, By.ID, 'EMAIL', config.email)

# escrever(navegador, By.ID, 'CEP', cep)
# escrever(navegador, By.ID, 'ENDERECO_NUMERO', config.numero)
# escrever(navegador, By.ID, 'COMPLEMENTO', config.complemento)
# escrever(navegador, By.ID, 'ENDERECO_TELEFONE', config.telefone)
# # clicar(navegador, By.ID, 'save')

# janela_atual = navegador.current_window_handle
# navegador.switch_to.window(janela_atual)

# limpar(navegador, By.ID, 'contratante0_ContratantePFNome')
# clicar(navegador, By.ID, 'myCont0')
# escrever(navegador, By.ID, 'contratante0_CampoContratantePFNome', config.nome)

clicar(navegador, By.ID, 'proprietario0_AproveitaDados')
escrever(navegador, By.ID, 'CONTRATO_NUMERO', config.ordem_de_servico)
escrever(navegador, By.ID, 'CONTRATO_DATAINICIO0', config.datahj)
escrever(navegador, By.ID, 'CONTRATO_DATAFIM0', config.data_final)
pyautogui.press('enter')
sleep(1)
escrever(navegador, By.ID, 'CONTRATO_VALOR0', config.valor)
clicar(navegador, By.CSS_SELECTOR, '#evtContratoEnderecoContainerSpecific0 > div:nth-child(3) > input:nth-child(1)')

clicar(navegador, By.ID, 'ESCOLHERCORDENADASGMAP')

trocar_janela_ativa(navegador)
fechar_janelas_extras(navegador)

#VALIDACAO
clicar(navegador, By.ID, 'code')