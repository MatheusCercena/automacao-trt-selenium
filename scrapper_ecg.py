from selenium.webdriver.common.by import By
import re
from acoes import *
from time import sleep
from cep_api import busca_cep, validar_cep

def login_ecg(navegador, usuario, senha):
    navegador.get('https://ecgglass.com/ecg_glass/login/login.php')
    escrever(navegador, By.NAME, 'text_usuario', usuario)
    escrever(navegador, By.NAME, 'password_senha', senha)
    clicar(navegador, By.CSS_SELECTOR, 'html body#bg_login_full div.container div#box_login_full form div.box_input.text-right input.btn.btn-primary')

def acessar_ordem_servico(navegador, ordem_de_servico):
    url = 'https://ecgglass.com/ecg_glass/geral/busca.php'
    if not navegador.current_url == url:
        navegador.get(url)
    escrever(navegador, By.ID, 'text_numero_os',ordem_de_servico)
    clicar(navegador, By.CSS_SELECTOR, 'div.formulario_filtro:nth-child(6) > div:nth-child(2) > input:nth-child(1)')

def acessar_orcamento(navegador, numero_orcamento):
    url = 'https://ecgglass.com/ecg_glass/geral/busca.php'
    if not navegador.current_url == url:
        navegador.get(url)
    escrever(navegador, By.ID, 'text_numero_orcamento', numero_orcamento)
    clicar(navegador, By.CSS_SELECTOR, 'div.formulario_filtro:nth-child(4) > div:nth-child(2) > input:nth-child(1)')

def acessar_dados_cliente(navegador, ordem_de_servico):
    url = 'https://ecgglass.com/ecg_glass/geral/busca.php'
    if not navegador.current_url == url:
        navegador.get(url)
    escrever(navegador, By.ID, 'text_numero_os', ordem_de_servico)
    clicar(navegador, By.CSS_SELECTOR, 'div.formulario_filtro:nth-child(6) > div:nth-child(2) > input:nth-child(1)')
    clicar(navegador, By.CSS_SELECTOR, 'a.f_16:nth-child(1)')
    clicar(navegador, By.CSS_SELECTOR, '.f_16 > b:nth-child(1)')

def pegar_dados_obra(navegador, ordem_de_servico, numero_orcamento):
    '''
    retorna um dicionario, com os itens 'area', 'cor', 'vidro' e preco.
    '''
    url_parcial = 'https://ecgglass.com/ecg_glass/ordemServico/cadOrdemServico.php?tipo=view&cod='
    if url_parcial not in navegador.current_url:
        acessar_ordem_servico(navegador, ordem_de_servico)
    WebDriverWait(navegador, 10).until(lambda d: d.execute_script("return document.readyState") == "complete") 
    area = pegar_texto(navegador, By.CSS_SELECTOR, 'div.col-12:nth-child(7)')
    area = re.sub(r'\D', '', area)
    clicar(navegador, By.ID, 'item_menu_dinamico_0')
    cor = 'seguindo padrao de cor das esquadrias do prédio'
    vidro = ''
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
                cor = pegar_texto(navegador, By.CSS_SELECTOR, '.ml-3 > b:nth-child(1)').lower()
                vidro = pegar_texto(navegador, By.CSS_SELECTOR, 'div.row:nth-child(3) > div:nth-child(1) > label:nth-child(1) > b:nth-child(1)').lower()
                break
    acessar_orcamento(navegador, numero_orcamento)
    preco = pegar_texto(navegador, By.CSS_SELECTOR, 'html body div table.table tbody tr td table tbody tr td.tabelaSubCorpo b')
    preco = re.sub(r'\D', '', preco)
    dados_obra = {
        'area' : area, 
        'cor' : cor, 
        'vidro' : vidro, 
        'preco' : preco
        }
    return dados_obra

def pegar_dados_cliente(navegador, ordem_de_servico):
    '''
    retorna um dicionario, com os itens 'nome', 'cpf', 'email', 'cep', 'numero', 'complemento' e 'telefone'.
    '''
    url_parcial = 'https://ecgglass.com/ecg_glass/pessoa/informacao.php?cod_pes='
    if url_parcial not in navegador.current_url:
        acessar_dados_cliente(navegador, ordem_de_servico)
    WebDriverWait(navegador, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    nome = pegar_texto(navegador, By.CSS_SELECTOR, '.font-weight-bold').title()
    fantasia = pegar_texto(navegador, By.CSS_SELECTOR, 'form.row:nth-child(1) > div:nth-child(5) > span:nth-child(2)').title()
    cpf = pegar_texto(navegador, By.CSS_SELECTOR, 'form.row:nth-child(1) > div:nth-child(6) > span:nth-child(2)').replace('.', '').replace('-', '').replace('/', '')
    email = pegar_texto(navegador, By.CSS_SELECTOR, 'form.formulario_cadastro:nth-child(3) > div:nth-child(5) > span:nth-child(2) > a:nth-child(1)').lower()
    dados_cliente = {
    'nome' : nome,
    'fantasia' : fantasia,
    'cpf' : cpf,
    'email' : email,
    }
    return dados_cliente

def pegar_endereco_cliente(navegador, ordem_de_servico):
    '''
    retorna um dicionario, com os itens 'cep', 'numero', 'complemento' e 'telefone'.
    '''
    url_parcial = 'https://ecgglass.com/ecg_glass/pessoa/informacao.php?cod_pes='
    if url_parcial not in navegador.current_url:
        acessar_dados_cliente(navegador, ordem_de_servico)
    WebDriverWait(navegador, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    # uf = pegar_texto(navegador, By.CSS_SELECTOR, 'form.formulario_cadastro:nth-child(3) > div:nth-child(7) > span:nth-child(2)')
    # cidade = pegar_texto(navegador, By.CSS_SELECTOR, 'form.formulario_cadastro:nth-child(3) > div:nth-child(8) > span:nth-child(2)')
    # logradouro = pegar_texto(navegador, By.CSS_SELECTOR, 'form.formulario_cadastro:nth-child(3) > div:nth-child(10) > span:nth-child(2) > a:nth-child(1)').strip().replace('.', '')
    cep = pegar_texto(navegador, By.CSS_SELECTOR, 'form.formulario_cadastro:nth-child(3) > div:nth-child(6) > span:nth-child(2)')

    while validar_cep(cep) == False:
        cep = ('Não conseguimos localizar o CEP válido, necessario inserir manualmente ao lado: ')

    # if len(cep) != 8:
    #     # cep = busca_cep(uf, cidade, logradouro)
    #     input = ('Não conseguimos localizar o CEP, ele tem menos de 8 digitos, necessario inserir manualmente')
    
    numero = pegar_texto(navegador, By.CSS_SELECTOR, 'form.formulario_cadastro:nth-child(3) > div:nth-child(11) > span:nth-child(2)')
    complemento = pegar_texto(navegador, By.CSS_SELECTOR, 'div.campo:nth-child(12) > span:nth-child(2)').title()
    telefone = pegar_texto(navegador, By.CSS_SELECTOR, 'form.formulario_cadastro:nth-child(3) > div:nth-child(4) > span:nth-child(2) > a:nth-child(1)')
    endereco_cliente = {
    'cep' : cep,
    'numero' : numero,
    'complemento' : complemento,
    'telefone' : telefone
    }
    return endereco_cliente

def pegar_endereco_extra(navegador, ordem_de_servico):
    url_parcial = 'https://ecgglass.com/ecg_glass/pessoa/informacao.php?cod_pes='
    if url_parcial not in navegador.current_url:
        acessar_dados_cliente(navegador, ordem_de_servico)
    WebDriverWait(navegador, 10).until(lambda d: d.execute_script("return document.readyState") == "complete")
    clicar(navegador, By.ID, 'endereco-instalacao-tab')
    endereco_cliente = {
        'cep' : '',
        'numero' : '',
        'complemento' : '',
        'telefone' : ''
        }
    try:
        cep = pegar_texto(navegador, By.CSS_SELECTOR, '#endereco-instalacao > form:nth-child(2) > div:nth-child(6) > span:nth-child(2)')
        numero = pegar_texto(navegador, By.CSS_SELECTOR, '#endereco-instalacao > form:nth-child(2) > div:nth-child(11) > span:nth-child(2)')
        complemento = pegar_texto(navegador, By.CSS_SELECTOR, '#endereco-instalacao > form:nth-child(2) > div:nth-child(12) > span:nth-child(2)').title()
        telefone = pegar_texto(navegador, By.CSS_SELECTOR, '#endereco-instalacao > form:nth-child(2) > div:nth-child(4) > span:nth-child(2) > a:nth-child(1)')
        endereco_cliente = {
        'cep' : cep,
        'numero' : numero,
        'complemento' : complemento,
        'telefone' : telefone
        } 
        return endereco_cliente
    except:
        return endereco_cliente

def pegar_endereco_folha(navegador, ordem_de_servico):
    url_parcial = 'https://ecgglass.com/ecg_glass/ordemServico/cadOrdemServico.php?tipo=view&cod='
    if url_parcial not in navegador.current_url:
        acessar_ordem_servico(navegador, ordem_de_servico)
    WebDriverWait(navegador, 10).until(lambda d: d.execute_script("return document.readyState") == "complete") 
    sleep(1)
    
    esperar_ajax(navegador)
    espera_objeto = WebDriverWait(navegador, 10)
    espera_objeto.until(EC.element_to_be_clickable((By.ID, 'select_geral')))

    mais_opcoes = navegador.find_element(By.ID, 'select_geral')
    combo_box = Select((mais_opcoes))
    combo_box.select_by_visible_text('Folha de rosto')

    esperar_ajax(navegador)
    espera_objeto = WebDriverWait(navegador, 10)
    espera_objeto.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[2]/div[2]/div/div[2]')))

    dados_endereco = {
    'cep' : '',
    'numero' : '',
    'complemento' : '',
    'telefone' : ''
    }

    spans = navegador.find_elements(By.TAG_NAME, 'span')
    for span in spans:
        if 'Endereço:' in span.text:
            texto_endereco = span.text
            texto_endereco = texto_endereco[10:]

            dados_endereco['numero'] = texto_endereco.split('-')[1].strip()
            dados_endereco['cep'] = texto_endereco.split('-')[4].strip()
            dados_endereco['complemento'] = texto_endereco.split('-')[-1][8:].strip().title()
            break

    for span in spans:
        if 'Fone:' in span.text:
            telefone = span.text
            texto_telefone = telefone[6:].title()
            dados_endereco['telefone'] = texto_telefone
            break
    return dados_endereco

