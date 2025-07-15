from acoes import *
from time import sleep
from urllib.parse import urljoin
from selenium.common.exceptions import NoSuchElementException

def dar_baixa(navegador):

    link = 'https://servicos.sinceti.net.br/app/view/sight/main?form=PesquisarART'
    navegador.get(link)


    clicar(navegador, By.ID, 'LISTARTS_totais')
    clicar(navegador, By.ID, 'save')
    clicar(navegador, By.CSS_SELECTOR, '#resultFiltro > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > a:nth-child(3)')
    sleep(1)
    selecionar_combo_box(navegador, By.XPATH, '/html/body/div[2]/div[3]/div/form/div[6]/div[2]/div[5]/div[1]/div[1]/label/select', '-1')
    lista = navegador.find_elements(By.XPATH,'/html/body/div[2]/div[3]/div/form/div[6]/div[2]/div[5]/div[2]/div/table/tbody/tr')
    lista_de_links = []
    lista_de_nomes = []
    for index in range(len(lista)):
        if (index + 1)%2 == 1: #ímpar 
            elemento = navegador.find_element(By.CSS_SELECTOR, f'tr.odd:nth-child({index+1}) > td:nth-child(12) > a:nth-child(1)')
        if (index + 1)%2 == 0: #par 
            elemento = navegador.find_element(By.CSS_SELECTOR, f'tr.even:nth-child({index+1}) > td:nth-child(12) > a:nth-child(1)')
        # nome_obj = navegador.find_element(By.XPATH, f'/html/body/div[2]/div[3]/div/form/div[6]/div[2]/div[5]/div[2]/div/table/tbody/tr[1]/td[9]')
        # nome = nome_obj.text 
        link_base = 'https://servicos.sinceti.net.br/app/view/sight/'
        resto_do_link = elemento.get_attribute("href")
        link_completo = urljoin(link_base, resto_do_link)
        lista_de_links.append(link_completo)
        # lista_de_nomes.append(nome)

    for link in lista_de_links:
        navegador.get(link)
        try:
            clicar(navegador, By.ID, 'baixarDocumento')
            clicar(navegador, By.ID, 'declaracaoAcessibilidade')
            selecionar_combo_box(navegador, By.ID, 'MOTIVO', '5')
            botoes = navegador.find_elements(By.CSS_SELECTOR, '.botao_adicionar')
            botao = botoes[1]
            botao_id = botao.get_attribute("id")
            clicar(navegador, By.ID, botao_id)
            sleep(1)
            clicar(navegador, By.ID, 'popup_ok')
            sleep(1.5)
            print(f'Baixa concluída da TRT {lista_de_nomes[index]}')
        except:
            print('Houve um erro ao dar baixa.')
            # try:
            #     existe = navegador.find_element(By.ID, 'botao_excluir')
            # except NoSuchElementException:
            #     existe = False
            # if existe == False:
            #     print(f'Houve um erro ao dar baixa {lista_de_nomes[index]}')
            # else:
            #     print(f'TRT {lista_de_nomes[index]} ja foi solicitada baixa')
            continue

