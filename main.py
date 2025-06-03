from selenium import webdriver
import time
navegador = webdriver.Firefox()

# navegador.get('https://servicos.sinceti.net.br/')
# navegador.maximize_window()

# login = navegador.find_element('id', 'login')
# login.click()
# login.send_keys('12676911902')

# senha = navegador.find_element('id', 'senha')
# senha.click()
# senha.send_keys('mdvHxi65')

# selecionar uma aba

# abas = navegador.window_handles
# navegador.switch_to.window(abas[1])

navegador.get('https://servicos.sinceti.net.br/app/view/sight/ini?form=Pessoal&login=12676911902')