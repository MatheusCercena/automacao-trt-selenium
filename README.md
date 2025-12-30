# Selenium TRT Automation

Automação de processos TRT (Termos de Responsabilidade Técnica) usando Selenium para os sistemas SINCETI e ECG Glass.

## 🚀 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/selenium-trt-automation.git
cd selenium-trt-automation
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## ⚙️ Configuração

1. Copie o arquivo de exemplo:
```bash
cp config.example.py config.py
```

2. Edite o arquivo `config.py` com suas credenciais:
```python
usuario_ecg = 'seu_usuario_ecg'
senha_ecg = 'sua_senha_ecg'
usuario_sinceti = 'seu_usuario_sinceti'
senha_sinceti = 'sua_senha_sinceti'
```

## 📖 Como usar

Execute o arquivo principal:
```bash
python main.py
```

## 🛠️ Funcionalidades

Cadastrar novas TRTs
Dar baixa nas TRTs
Automação de login nos sistemas
Preenchimento automático de formulários
