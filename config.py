import gender_api
from datetime import datetime
from dateutil.relativedelta import relativedelta
from scrapper import login_ecg, pegar_dados_obra, pegar_dados_cliente

# ADMIN
usuario_ecg = 'matheusversatil'
senha_ecg = 'matheus.versatil'
usuario_sinceti = '12676911902'
senha_sinceti = 'mdvHxi65'

# GERAL
ordem_de_servico = '404/25-1'
numero_orcamento = ordem_de_servico[:-2]
dados_obra = pegar_dados_obra(numero_orcamento)
dados_cliente = pegar_dados_cliente(ordem_de_servico)

#SCRAPPING - DADOS DA OBRA
area = int(str(dados_obra['area'])+'000')
vidro = dados_obra['vidro']
cor_aluminio = dados_obra['cor']
valor = int(str(dados_obra['preco'])+'00')
cores_anodizadas = ['BRONZE1002 ANODIZADO', 'INOX JATEADO', 'NAT. FOSCO']
processo = ['anodizada' if cor_aluminio in [cores_anodizadas] else 'pintada']

#SCRAPPING - DADOS DO CLIENTE
nome = dados_cliente['nome']
cpf = dados_cliente['cpf']
email = dados_cliente['email']
telefone = dados_cliente['telefone']
genero = gender_api.define_gender(nome)
cep = dados_cliente['cep']
numero = dados_cliente['numero']
complemento = dados_cliente['complemento']

# PREENCHIMENTO
datahj = datetime.today().strftime('%d%m%y')
data_final = (datetime.today() + relativedelta(months=2)).strftime('%d%m%y')
obs = f'Envidraçamento de sacada com vidro liso {vidro} e esquadrias de aluminio {processo} na cor {cor_aluminio}.'

dados = {}


# #CONFIG
# usuario_ecg = 'matheusversatil'
# senha_ecg = 'matheus.versatil'
# usuario_sinceti = '12676911902'
# senha_sinceti = 'mdvHxi65'

# #INPUTS
# ordem_de_servico = '460/25-1'

# #SCRAPPING - OS
# area = int(str(10)+'000')

# #SCRAPPING - ORÇAMENTO
# vidro = 'incolor temperado'
# cor_aluminio = 'branco'
# valor = int(str(5000)+'00')

# #SCRAPPING - DADOS DO CLIENTE
# nome = 'Marcelo Germano'
# cpf = '12345678900'
# email = 'email'
# cep = 12345678
# numero = 1234
# complemento = 'Rua Tal Tal Tal, Residencial Tal'
# telefone = 48998765432

# #LOGICA
# datahj = '060625'
# data_final = '060825'
# obs = f'Envidraçamento de sacada com vidro liso {vidro} e esquadrias de aluminio {processo} de {cor_aluminio}.'
# processo = 'pintada'
# genero = gender_api.data
