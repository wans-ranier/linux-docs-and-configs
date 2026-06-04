##Como acesso os aquivos no do meu celular conectado por USB?##
Para localizar um celular Android conectado via USB no Ubuntu ou Pop!_OS, o método mais direto é verificar o sistema de arquivos virtual que monta automaticamente o dispositivo via protocolo MTP. Você pode encontrar o caminho exato executando o seguinte comando no terminal:

``bash
 find /run/user/*/gvfs -maxdepth 1 -name 'mtp:*'   
``                                                                                  

Ocomando retornará o caminho da pasta onde os arquivos do celular estão acessíveis.
[...]
Caso precise de ferramentas de linha de comando ou o gerenciador de arquivos não exiba o dispositivo, instale os pacotes de suporte ao MTP e ADB:

``bash
sudo apt install mtp-tools gmtp android-tools-adb
``
Após a instalação, você pode verificar se o sistema reconhece o dispositivo usando `adb devices` ou abrir o gerenciador de arquivos gMTP para navegar pelas pastas manualmente. 
