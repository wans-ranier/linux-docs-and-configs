**Como criar Hard Links no Sistema de Arquivos**

Nesse guia, vou mostrar como se cria esse tipo de link e como se diferencia do `Soft Link` (ou `Symbolic Link`) que mencionei em outra notação. Ao contrário de um Soft Link, que é um ponteiro para um nome de arquivo, um `Hard Link` é outro nome para o próprio arquivo. Ambos os nomes apontam diretamente para os mesmos dados no disco, que são identificados por um número único chamado inode.

Vamos usar os mesmos arquivos do que foi praticado no `how2create-Files-symlink-with-vi.md`, vai estar na pasta `example`.

O primeiro passo vai ser criar o Hard Link chamado `notaC`, usando o comando `ln` para apontar para o mesmo inode de `notaA`, mas sem a opção `-s`, que servia para criar o soft link.
```bash
ln notaA notaC
```

Observe o conteúdo dos três arquivos criados. Execute os comandos:
```bash
cat notaA
cat notaB
cat notaC
#Você verá o mesmo conteúdo impresso três vezes, o que é esperado
```
Qual a diferença entre os dois? Isso fica mais claro quando analisamos as suas propriedades e seus inodespor meio do comando `ls -il` de novo.
```bash
ls -il nota[A-C]
``
O resultado será semelhante a isso. Olhe atentamente a primeira e a segunda coluna:
```plaintext
1444200 -rw-rw-r-- 2 wansranier wansranier 10 mai 14 15:43 notaA
1442191 lrwxrwxrwx 1 wansranier wansranier  5 mai 14 15:52 notaB -> notaA
1444200 -rw-rw-r-- 2 wansranier wansranier 10 mai 14 15:43 notaC
```
Vamos analisar o resultado:
 1. `Números de Inode (Coluna 1)`: Observe que os arquivos `notaA` e `notaC` possuem exatamente o mesmo número de inode (por exemplo, 131075). Essa é a característica que define um link físico. Eles não são arquivos separados; são dois nomes diferentes apontando para os mesmos dados de arquivo no disco. O link simbólico fileb possui seu próprio inode exclusivo.

 2. `Contagem de links (coluna 2)`: Observe o número para `notaA` e `notaC`. Agora é 2. Esse número representa a contagem de links físicos e indica quantos nomes (links físicos) apontam para esse único inode. Quando você criou o arquivo `notaC`, a contagem de links para esse inode aumentou de 1 para 2.
 
 3. `Tipo de arquivo (coluna 1 das permissões)`: Observe que o arquivo `notaC` está listado como um arquivo comum (suas permissões começam com -), assim como o arquivo `notaA`. Ele não é um tipo de link especial como o arquivo `notaB` (que começa com l).

