# 01 - Introdução a Testes Automatizados com Pytest

Módulo introdutório com exemplos práticos de testes unitários em Python utilizando o framework **pytest**.

---

## 📋 Pré-requisitos

Antes de executar os testes, certifique-se de configurar o ambiente virtual (`venv`) e instalar o `pytest`.

> 🔗 Para instruções detalhadas de configuração de ambientes virtuais, consulte:  
> **[Tutorial de Criação e Uso de venv](../../../fundamentos/python/howInstall-venv-setup.md)**

### Ativando o Ambiente e Instalando Dependências

```bash
# 1. Ative seu ambiente virtual
source venv/bin/activate

# 2. Instale o pytest no ambiente
pip install pytest
```

## Como executar

```bash
# Executar todos os testes da pasta com saída detalhada
pytest -v

# Executar apenas um arquivo específico
pytest -v test_soma.py

# Filtrar e rodar apenas testes que contenham "soma" no nome
pytest -v -k "soma"

# Executar testes exibindo o motivo (reason) dos testes ignorados (skipped)
pytest -v -rs test_skip.py
```
