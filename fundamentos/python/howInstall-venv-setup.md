**Configuração de Ambiente Virtual Python com `venv` no Linux**

Esse é um guia para configurar um ambiente virtual Python usando `venv` no Linux. Antes de usar qualquer comando para instalar(como o `pip`), é necessario criar um ambiente que impede que a instalação de pacotes que afete o sistema global das configurações do python3 da maquina.

 O `venv` é uma ferramenta que permite criar ambientes isolados para projetos Python, garantindo que as dependências de cada projeto não interfiram umas com as outras.

## Passos para Configurar o Ambiente Virtual
1. **Instalar o Python3 e o `venv`**:
   Certifique-se de que o Python3, módulo `venv` e o pip estão instalados no seu sistema. Você pode instalar usando o seguinte comando:
   ```bash
   sudo apt update
   sudo apt install python3-venv
   sudo apt install python3-pip
   
    # Verifique as instalações
    python3 --version
    pip3 --version
   ```
2. **Criar um Ambiente Virtual**:
   Navegue até o diretório do seu projeto e crie um ambiente virtual usando o comando:
   ```bash
   python3 -m venv nome_do_ambiente_virtual
    ```

3. **Ativar o Ambiente Virtual**:
   Para ativar o ambiente virtual, copie e execute o seguinte comando:
   ```bash
   source venv1/bin/activate
   ```
   Após a ativação, você verá o nome do ambiente virtual no prompt do terminal, indicando que está usando o ambiente isolado. Exemplo:
   ```bash
   (venv1)user@ubuntu:~/projects/my_python_project$
	```

	Verifique se você está usando o python do ambiente virtual:
	```bash
	Which python
	#Output:/home/user/projects/my_python_project/venv/bin/python

	which pip
	#Output: /home/user/projects/my_python_project/venv/bin/pip`
	```

4. **Instalar pacotes com pip**
   Com o ambiente instalado, agora pode instalar os pacotes com o comando pip:
   ```bash
	# Garanta que seu ambiente virtual esteja ativado primeiro
	source venv/bin/activate

	#Instale um único pacote (versão mais recente)
	pip install requests

	# Instale uma versão específica de um pacote
	pip install requests==2.31.0

	# Instale uma versão mínima
	pip install "requests>=2.28.0"

	# Instale vários pacotes de uma vez
	pip install flask sqlalchemy redis

	# Instale um pacote com dependências opcionais (extras)
	pip install "fastapi[all]"
   ```
5.  **Checar e Desativar o Ambiente virtual**
 Checar se está ativado:  
   ```bash
# Verifique se um ambiente virtual está ativo

echo $VIRTUAL_ENV

# Saída: /home/user/projects/my_python_project/venv

# Se nenhum ambiente virtual estiver ativo, a saída ficará vazia

# Método alternativo: verifique a localização do Python

python -c "import sys; print(sys.prefix)"

# Deve mostrar o caminho do seu venv quando ativado
```
 Agora como desativar:
 ```bash
# Desative o ambiente virtual e retorne ao Python do sistema

deactivate

# Seu prompt retorna ao normal:
# user@ubuntu:~/projects/my_python_project$

# Verifique a desativação

which python

# Saída: /usr/bin/python3 (ou caminho do sistema similar)
```

Essa é a minha forma de instalar bibliotecas python no linux. Esse tutorial vai lhe dar  o essencial para configurar o seu projeto e ir codificar. Espero que isso tenha ajudado, obrigado pela atenção.
