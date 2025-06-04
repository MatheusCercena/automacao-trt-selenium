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

sleep(3)
confirmacao = navegador.find_element(By.CLASS_NAME, "ajs-ok") 
confirmacao.click()

sleep(3)
forma_registro = navegador.find_element(By.ID, "FORMADEREGISTRO")
forma = Select(forma_registro)
forma.select_by_value('5')

sleep(3)
finalidade = navegador.find_element(By.ID, "FINALIDADE")
navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", finalidade)
fin = Select(finalidade)
fin.select_by_value('29')





# selecionar uma aba

# abas = navegador.window_handles
# navegador.switch_to.window(abas[1])
