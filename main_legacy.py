# from preenchimento_trt import login_sinceti
# from scrapper_ecg import login_ecg
# from config import senha_ecg, senha_sinceti, usuario_ecg, usuario_sinceti
# from threading import Thread
# from queue import Queue, Empty

# def scrapper(navegador, lista_de_pedidos: Queue, lista_de_dados: Queue):
#     """Pega dados no ECG enquanto houver OS na fila."""
#     while True:
#         ordem_de_servico = lista_de_pedidos.get()
#         if ordem_de_servico is None:
#             lista_de_pedidos.task_done()
#             break
#         try:
#             dados = criar_dados(navegador, ordem_de_servico)
#             lista_de_dados.put(dados)
#             print(dados)
#         finally:
#             lista_de_pedidos.task_done()

# if __name__ == "__main__":
#     lista_de_pedidos, lista_de_dados = Queue(), Queue()

#     # 1. Adiciona as OSs na da lista de pedidos
#     print('Insira abaixo as Ordens de Serviço das TRTs a serem feitas, lembrando que após abrir o navegador você terá 15 segundos para inserir a validação do login no SINCETI.')
#     for ordem_de_servico in solicitar_ordens_de_servico():
#         lista_de_pedidos.put(ordem_de_servico)

#     # 2. Abre os navegadores e faz os logins
#     navegador_ecg = abrir_navegador(True)
#     login_ecg(navegador_ecg, usuario_ecg, senha_ecg)
    
#     # 3. Cria a thread de busca de dados no ecg
#     t = Thread(target=scrapper,
#                args=(navegador_ecg, lista_de_pedidos, lista_de_dados),
#                daemon=True)
#     t.start()
    
#     navegador_sinceti = abrir_navegador(False)
#     login_sinceti(navegador_sinceti, usuario_sinceti, senha_sinceti)

#     # 4. Quando pode pegar um dado na fila, preenche a trt com os dados e remove a tarefa da fila
#     while True:
#         try:
#             dados = lista_de_dados.get(timeout=1)
#         except Empty:
#             if lista_de_pedidos.empty() and not t.is_alive():
#                 break
#             continue
#         link = 'https://servicos.sinceti.net.br/app/view/sight/ini?form=Art&id=5717331'
#         navegador_sinceti.get(link)
#         preencher_trts(navegador_sinceti, dados)
#         lista_de_dados.task_done()

#     #após finalizar todos os pedidos e a lista de tarefas estar vazia, finaliza tudo
#     lista_de_pedidos.put(None)
#     t.join()
#     lista_de_pedidos.join()
#     lista_de_dados.join()

#     navegador_ecg.quit()
#     navegador_sinceti.quit()
