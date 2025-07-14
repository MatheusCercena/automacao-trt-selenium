from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from time import sleep

def esperar_ajax(navegador):
    espera = WebDriverWait(navegador, 10)
    espera.until(EC.invisibility_of_element_located((By.ID, "ajax-overlay")))

def selecionar_combo_box(navegador, tipo_seletor, seletor, valor):
    esperar_ajax(navegador)
    espera_objeto = WebDriverWait(navegador, 10)
    espera_objeto.until(EC.element_to_be_clickable((tipo_seletor, seletor)))
    objeto = navegador.find_element(tipo_seletor, seletor)
    combo_box = Select((objeto))
    combo_box.select_by_value(valor)

def clicar(navegador, tipo_seletor, seletor):
    esperar_ajax(navegador)
    espera_objeto = WebDriverWait(navegador, 10)
    espera_objeto.until(EC.element_to_be_clickable((tipo_seletor, seletor)))
    objeto = navegador.find_element(tipo_seletor, seletor)
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", objeto)
    objeto.click()

def escrever(navegador, tipo_seletor, seletor, key):
    esperar_ajax(navegador)
    espera_objeto = WebDriverWait(navegador, 10)
    espera_objeto.until(EC.element_to_be_clickable((tipo_seletor, seletor)))
    objeto = navegador.find_element(tipo_seletor, seletor)
    navegador.execute_script("arguments[0].scrollIntoView({block: 'center'})", objeto)
    objeto.send_keys(key)

def trocar_janela_ativa(navegador):
    WebDriverWait(navegador, 10).until(EC.number_of_windows_to_be(2))
    janelas = navegador.window_handles
    navegador.switch_to.window(janelas[1])
    WebDriverWait(navegador, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

def fechar_janelas_extras(navegador):
    navegador.close()
    navegador.switch_to.window(navegador.window_handles[0])

def pegar_texto(navegador, tipo_seletor, seletor):
    espera_objeto = WebDriverWait(navegador, 3)
    espera_objeto.until(EC.element_to_be_clickable((tipo_seletor, seletor)))
    objeto = navegador.find_element(tipo_seletor, seletor)
    return objeto.text
