from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


profile_path = "C:\\Users\\Certheus\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles\\05llhb7i.automatization"
options = Options()
options.profile = profile_path

navegador = webdriver.Firefox(service=Service(), options=options)

navegador.get('https://servicos.sinceti.net.br/')
navegador.maximize_window()

login = navegador.find_element('id', 'login')
login.click()
login.send_keys('12676911902')

senha = navegador.find_element('id', 'senha')
senha.click()
senha.send_keys('mdvHxi65')

sleep(15)

navegador.get('https://servicos.sinceti.net.br/app/view/sight/main.php?form=CadastroART')

opcoes = navegador.find_element('id', 'TIPOART')
espera_opcoes = WebDriverWait(navegador, 100)
espera_opcoes.until(EC.element_to_be_clickable(opcoes))
opcoes.click()

servico = Select(opcoes)
servico.select_by_value('COD101')

# espera_confirmacao = WebDriverWait(navegador, 100)
# espera_confirmacao.until(EC.element_to_be_clickable(confirmacao))

espera_confirmacao = WebDriverWait(navegador, 100)
espera_confirmacao.until(EC.element_to_be_clickable((By.CLASS_NAME, "ajs-ok")))
confirmacao = navegador.find_element(By.CLASS_NAME, "ajs-ok") 
confirmacao.click()

espera = WebDriverWait(navegador, 100)
espera.until(EC.invisibility_of_element_located((By.ID, "ajax-overlay")))

espera_forma_registro = WebDriverWait(navegador, 100)
espera_forma_registro.until(EC.element_to_be_clickable((By.ID, 'FORMADEREGISTRO')))
forma_registro = navegador.find_element(By.ID, "FORMADEREGISTRO")
forma = Select(forma_registro)
forma.select_by_value('5')

esperar_ajax = WebDriverWait(navegador, 100)
esperar_ajax.until(EC.invisibility_of_element_located((By.ID, 'ajax-overlay')))

finalidade = navegador.find_element(By.ID, "FINALIDADE")
navegador.execute_script("arguments[0].scrollIntoView({block: 'start'})", finalidade)
espera_finalidade = WebDriverWait(navegador, 100)
espera_finalidade.until(EC.element_to_be_clickable(finalidade))
fin = Select(finalidade)
fin.select_by_value('29')


observaçao = navegador.find_element(By.ID, 'OBSERVACAO')
vidro = 'incolor temperado'
processo = 'pintada'
cor_aluminio = 'branco'
observaçao.send_keys(f'Envidraçamento de sacada com vidro liso {vidro} e esquadrias de aluminio {processo} de {cor_aluminio}.')

acao_inst = navegador.find_element(By.ID, 'ACAOINSTITUCIONAL')
acoes_inst = Select(acao_inst)
acoes_inst.select_by_value('17')

esperar_ajax = WebDriverWait(navegador, 100)
esperar_ajax.until(EC.invisibility_of_element_located((By.ID, 'ajax-overlay')))

novo_atividade = navegador.find_element(By.ID, 'NOVO_ATIVIDADE')
navegador.execute_script("arguments[0].scrollIntoView({block: 'start'})", novo_atividade)
novo_atividade.click()

espera_nivel_ativ = WebDriverWait(navegador, 100)
espera_nivel_ativ.until(EC.element_to_be_clickable((By.ID, 'NIVEL0')))
nivel_ativ = navegador.find_element(By.ID, 'NIVEL0')
niveis_ativ = Select(nivel_ativ)
niveis_ativ.select_by_value('1004')

ativ_prof = navegador.find_element(By.ID, 'ATIVIDADEPROFISSIONAL0')
atividades_prof = Select(ativ_prof)
atividades_prof.select_by_value('4200')

atuacao = navegador.find_element(By.ID, 'LABELATUACAO0')
atuacao.send_keys('1112')
espera_atuacao = WebDriverWait(navegador, 100)
espera_atuacao.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[3]/div/div/form/div[2]/div[4]/div[7]/div[1]/div/div[4]/div[1]/div[8]/div[3]/ul/li')))
fachada_mistos = navegador.find_element(By.XPATH, '/html/body/div[2]/div[3]/div/div[2]/div[3]/div/div/form/div[2]/div[4]/div[7]/div[1]/div/div[4]/div[1]/div[8]/div[3]/ul/li')
fachada_mistos.click()

unidade = navegador.find_element(By.ID, 'UNIDADE0')
unidades = Select(unidade)
unidades.select_by_value('2')

qntd = int(str(10)+'000')
quantidade = navegador.find_element(By.ID, 'QUANTIDADE0')
quantidade.send_keys(qntd)

novo_contrato = navegador.find_element(By.ID, 'NOVO_CONTRATO')
navegador.execute_script("arguments[0].scrollIntoView({block: 'start'})", novo_contrato)
novo_contrato.click()

espera_contratante = WebDriverWait(navegador, 100)
espera_contratante.until(EC.element_to_be_clickable((By.ID, 'contratante0_ContratantePFNome')))
contratante_pes_fis = navegador.find_element(By.ID, 'contratante0_ContratantePFNome')
contratante_pes_fis.click()

nome = 'Fulano de Tal'
espera_nome = WebDriverWait(navegador, 100)
espera_nome.until(EC.element_to_be_clickable((By.ID, 'contratante0_CampoContratantePFNome')))
nome_contratante = navegador.find_element(By.ID, 'contratante0_CampoContratantePFNome')
nome_contratante.send_keys(nome)


clique_fora = navegador.find_element(By.ID, 'myCont0')
clique_fora.click()

esperar_cadastro = WebDriverWait(navegador, 100)
esperar_cadastro.until(EC.element_to_be_clickable((By.CLASS_NAME, 'botao_adicionar')))
cadastrar = navegador.find_element(By.CLASS_NAME, 'botao_adicionar')
cadastrar.click()

janela_atual = navegador.current_window_handle
sleep(3)
janelas = navegador.window_handles
for janela in janelas:
    if janela != janela_atual:
        navegador.switch_to(janela)
        break



#criar funcao para selecionar e para clicar 

# selecionar uma aba

# abas = navegador.window_handles
# navegador.switch_to.window(abas[1])
