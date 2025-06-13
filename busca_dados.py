import gender_api
from datetime import datetime
from dateutil.relativedelta import relativedelta
from scrapper import login_ecg, pegar_dados_obra, pegar_dados_cliente
from config import senha_ecg, usuario_ecg

def criar_dados(ordem_de_servico):
    numero_orcamento = ordem_de_servico[:-2]
    login_ecg(usuario_ecg, senha_ecg)
    
    dados_obra = pegar_dados_obra(ordem_de_servico, numero_orcamento)
    dados_cliente = pegar_dados_cliente(ordem_de_servico)

    area = (dados_obra['area'])+'000'
    valor = (dados_obra['preco'])+'00'
    cores_anodizadas = ['BRONZE1002 ANODIZADO', 'INOX JATEADO', 'NAT. FOSCO']
    processo = 'anodizada' if dados_obra['cor'] in [cores_anodizadas] else 'pintada'
    genero = gender_api.define_gender(dados_cliente['nome'])
    datahj = datetime.today().strftime('%d%m%y')
    data_final = (datetime.today() + relativedelta(months=2)).strftime('%d%m%y')
    obs = f'Envidraçamento de sacada com {dados_obra['vidro']} e esquadrias de aluminio {processo} na cor {dados_obra['cor']}.'

    dados = {
        'nome' : dados_cliente['nome'],
        'genero' : genero,
        'cpf' : dados_cliente['cpf'],
        'email' : dados_cliente['email'],
        'cep' : dados_cliente['cep'],
        'numero' : dados_cliente['numero'],
        'complemento' : dados_cliente['complemento'],
        'telefone' : dados_cliente['telefone'],
        'area' : area, 
        'cor' : dados_obra['cor'], 
        'vidro' : dados_obra['vidro'], 
        'preco' : valor,
        'processo' : processo,        
        'obs' : obs,
        'data_inicial' : datahj,
        'data_final' : data_final
    }
    return dados