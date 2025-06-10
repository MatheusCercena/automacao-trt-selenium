from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import re
import config
from acoes import *

navegador = webdriver.Firefox(service=Service(), options=Options()) 

def login_ecg(navegador):       
    navegador.get('https://ecgglass.com/ecg_glass/login/login.php')
    navegador.maximize_window()
    escrever(navegador, By.NAME, 'text_usuario', config.usuario_ecg)
    escrever(navegador, By.NAME, 'password_senha', config.senha_ecg)
    clicar(navegador, By.CSS_SELECTOR, 'html body#bg_login_full div.container div#box_login_full form div.box_input.text-right input.btn.btn-primary')

def acessar_ordem_servico(navegador):
    url = 'https://ecgglass.com/ecg_glass/geral/busca.php'
    if not navegador.current_url == url:
        navegador.get(url)
    escrever(navegador, By.ID, 'text_numero_os', config.ordem_de_servico)
    clicar(navegador, By.CSS_SELECTOR, 'div.formulario_filtro:nth-child(6) > div:nth-child(2) > input:nth-child(1)')

def acessar_orcamento(navegador):
    url = 'https://ecgglass.com/ecg_glass/geral/busca.php'
    if not navegador.current_url == url:
        navegador.get(url)
    escrever(navegador, By.ID, 'text_numero_orcamento', config.ordem_de_servico)
    clicar(navegador, By.CSS_SELECTOR, 'div.formulario_filtro:nth-child(4) > div:nth-child(2) > input:nth-child(1)')

def acessar_dados_cliente(navegador: webdriver):
    url = 'https://ecgglass.com/ecg_glass/geral/busca.php'
    if not navegador.current_url == url:
        navegador.get(url)
    escrever(navegador, By.ID, 'text_numero_os', config.ordem_de_servico)
    clicar(navegador, By.CSS_SELECTOR, 'div.formulario_filtro:nth-child(6) > div:nth-child(2) > input:nth-child(1)')
    clicar(navegador, By.CSS_SELECTOR, 'a.f_16:nth-child(1)')
    clicar(navegador, By.CSS_SELECTOR, '.f_16 > b:nth-child(1)')

def pegar_dados_obra():
    
    pass

def dados_cliente(navegador: webdriver):
    url_parcial = 'https://ecgglass.com/ecg_glass/pessoa/informacao.php?cod_pes='
    if url_parcial not in navegador.current_url:
        acessar_dados_cliente(navegador)
    nome = pegar_texto(navegador, By.CSS_SELECTOR, '.font-weight-bold').title()
    cpf = pegar_texto(navegador, By.CSS_SELECTOR, 'form.row:nth-child(1) > div:nth-child(6) > span:nth-child(2)').replace('.', '').replace('-','')
    email = pegar_texto(navegador, By.CSS_SELECTOR, 'form.formulario_cadastro:nth-child(3) > div:nth-child(5) > span:nth-child(2) > a:nth-child(1)').lower()
    cep = pegar_texto(navegador, By.CSS_SELECTOR, 'form.formulario_cadastro:nth-child(3) > div:nth-child(6) > span:nth-child(2)')
    numero = pegar_texto(navegador, By.CSS_SELECTOR, 'form.formulario_cadastro:nth-child(3) > div:nth-child(11) > span:nth-child(2)')
    complemento = pegar_texto(navegador, By.CSS_SELECTOR, 'div.campo:nth-child(12) > span:nth-child(2)').title()
    telefone = pegar_texto(navegador, By.CSS_SELECTOR, 'form.formulario_cadastro:nth-child(3) > div:nth-child(4) > span:nth-child(2) > a:nth-child(1)')
    dados_obra = {
    'nome' : nome,
    'nome' : cpf,
    'nome' : email,
    'nome' : cep,
    'nome' : numero,
    'nome' : complemento,
    'nome' : telefone
    }
    return dados_obra



WebDriverWait(navegador, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")

AREA = pegar_texto(navegador, By.CSS_SELECTOR, 'div.col-12:nth-child(7)')
AREA = re.sub(r'\D', '', AREA)

clicar(navegador, By.CSS_SELECTOR, 'a.f_16:nth-child(1)')
clicar(navegador, By.CSS_SELECTOR, '.f_16 > b:nth-child(1)')


navegador.get(url)

escrever(navegador, By.ID, 'text_numero_orcamento', config.numero_orçamento)
clicar(navegador, By.CSS_SELECTOR, 'div.formulario_filtro:nth-child(4) > div:nth-child(2) > input:nth-child(1)')

PRECO = pegar_texto(navegador, By.CSS_SELECTOR, 'html body div table.table tbody tr td table tbody tr td.tabelaSubCorpo b')

navegador.back()
navegador.back()
navegador.back()
navegador.back()

clicar(navegador, By.ID, 'item_menu_dinamico_0')

COR = 'seguindo padrao de cor das esquadrias do prédio'
VIDRO = ''
listar_projetos = None

try:
    cor = pegar_texto(navegador, By.CSS_SELECTOR, '.ml-3 > b:nth-child(1)').lower()
    vidro = pegar_texto(navegador, By.CSS_SELECTOR, 'div.row:nth-child(3) > div:nth-child(1) > label:nth-child(1) > b:nth-child(1)').lower()

except:
    pass

try:
    listar_projetos = navegador.find_element(By.NAME, 'itemProj')
except:
    pass

if listar_projetos:
    lista = Select(listar_projetos)
    for serial in lista.options:
        if '1-SACADA-KAIZEN' in serial.text or '2-PORTAS-KAIZEN' in serial.text:
            value = serial.get_attribute('value')
            selecionar_combo_box(navegador, By.NAME, 'itemProj', value)
            COR = pegar_texto(navegador, By.CSS_SELECTOR, '.ml-3 > b:nth-child(1)').lower()
            VIDRO = pegar_texto(navegador, By.CSS_SELECTOR, 'div.row:nth-child(3) > div:nth-child(1) > label:nth-child(1) > b:nth-child(1)').lower()
            break
            
