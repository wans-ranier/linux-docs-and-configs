# Testes Automatizados com Selenium

Módulo com exemplos práticos de automação de navegador usando **Selenium WebDriver** com **Firefox (geckodriver)**.

---

## 📋 Pré-requisitos

### 1. Instalar o Firefox e o geckodriver

```bash
# Debian/Ubuntu
sudo apt install firefox

# Baixar o geckodriver (versão compatível com seu Firefox)
# https://github.com/mozilla/geckodriver/releases
# Extraia e coloque em um diretório conhecido, ex:
# /home/SEU_USUARIO/Documentos/geckodriver-v0.37.1-linux64/geckodriver
```

### 2. Configurar o ambiente virtual

```bash
# Criar venv (na raiz do projeto ou na pasta selenium)
python -m venv .venv
source .venv/bin/activate

# Instalar dependências
pip install -r requirements.txt
```

### 3. Configurar o `.env`

Crie um arquivo `.env` na **raiz do projeto** (`linux-docs-and-configs/.env`) com o caminho do geckodriver:

```env
PATH_DRIVE_BROWSER=/caminho/para/geckodriver
```

> ⚠️ O `.env` **não** é commitado (está no `.gitignore`). Use o `.env.example` como modelo.

---

## 📁 Estrutura

```
selenium/
├── requirements.txt          # Dependências (selenium, pytest, python-dotenv)
├── .env.example              # Modelo de variáveis de ambiente
├── mais_testes_comAssert.py  # Testes básicos com assert
├── teste-01.py               # Teste simples de navegação
├── teste-02.py               # Teste com back()/forward()
├── aula_DOM/                 # Exercícios de manipulação do DOM
│   ├── teste-rapido.py       # Seletores e extração de dados
│   ├── exercicio-1.py        # Espera explícita + elemento dinâmico
│   ├── exercicio-2.py        # Múltiplas abas
│   ├── exercicio-3.py        # Iframe + alerta + aba + invisibilidade
│   └── desfio_buscalistacatalago.py  # Catálogo de elementos
└── testes-paginasDinamicas/  # Páginas dinâmicas
    └── desafio.py
```

## Como executar

```bash
# Ativar venv
source .venv/bin/activate

# Executar um script específico
python automacao-scripts/Testes-Automatizados-Software/selenium/aula_DOM/testes-paginasDinamicas/exercicio3.py

# Executar com pytest (quando aplicável)
pytest -v automacao-scripts/Testes-Automatizados-Software/selenium/
```

## 🔑 Padrão de acesso ao driver

Todos os scripts usam o padrão `.env` para evitar expor caminhos locais:

```python
import os
from dotenv import load_dotenv
from selenium.webdriver.firefox.service import Service

load_dotenv()
driver_path = os.environ.get('PATH_DRIVE_BROWSER')
service = Service(driver_path)
driver = webdriver.Firefox(service=service)
```

> Nunca use caminhos hardcoded como `Service("/home/.../geckodriver")`. Use sempre a variável de ambiente.