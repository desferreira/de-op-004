# PROJETO FINAL - VERSIONAMENTO E ARQUIVOS DE MARCAÇÃO

Você foi contratado como desenvolvedor da Amazon e a sua primeira tarefa foi desenvolver um programa que precisa integrar com vários sistemas externos, os produtos estão armazenados em um arquivo csv. Por ser um programa que vai ser utilizado por outras pessoas do time, é essecial que seja seguido algum padrão de desenvolvimento do Git, para que a contribuição seja o mais fluída possivel. O programa deve ler os produtos que foram vendidos pela Amazon e gerar a saída em 3 formatos diferentes, um para cada sistema externo: XML, JSON e YAML. O controle do “tipo” de saída pode ser feito via variáveis de chamada, ou seja:
- Se a saída for em XML, posso chamar o programa com python `gerador-nf.py –formato=xml`

- Se a saída for em JSON, posso chamar o programa com python `gerador-nf.py —formato=json`

- Se a saída for em JSON, posso chamar o programa com python `gerador-nf.py —formato=yaml`


Exemplo: 

**Entrada CSV**
```
nome,preco,quantidade,marca,cod_barra,imposto
"Iphone14",7500,2,Apple,3123123712,135
"PS5",3500,2,Sony,43436,250
"Camiseta Lacoste",450,2,Lacoste,454543,100
"Tablet Galaxy",1100,2,Samsung,12312,356
```
**Saída XML**
```
<listaDeProdutos>
    <produto>
        <produto>Iphone14</produto>
        <preco>7500</preco>
        <quantidade>2</quantidade>
        <marca>Apple</marca>
        <cod_barra>3123123712</cod_barra>
        <imposto>135</imposto>
    </produto>
    <produto>
        <produto>PS5</produto>
        <preco>3500</preco>
        <quantidade>2</quantidade>
        <marca>Sony</marca>
        <cod_barra>43436</cod_barra>
        <imposto>250</imposto>
    </produto>
    <produto>
        <produto>Camiseta Lacoste</produto>
        <preco>450</preco>
        <quantidade>2</quantidade>
        <marca>Lacoste</marca>
        <cod_barra>454543</cod_barra>
        <imposto>100</imposto>
    </produto>
    <produto>
        <produto>Tablet Galaxy</produto>
        <preco>1100</preco>
        <quantidade>2</quantidade>
        <marca>Samsung</marca>
        <cod_barra>12312</cod_barra>
        <imposto>356</imposto>
    </produto>
</listaDeProdutos>
```
**Saída YAML**
```
- cod_barra: '3123123712'
imposto: '135'
marca: Apple
nome: Iphone14
preco: '7500'
quantidade: '2'
- cod_barra: '43436'
imposto: '250'
marca: Sony
nome: PS5
preco: '3500'
quantidade: '2'
- cod_barra: '454543'
imposto: '100'
marca: Lacoste
nome: Camiseta Lacoste
preco: '450'
quantidade: '2'
- cod_barra: '12312'
imposto: '356'
marca: Samsung
nome: Tablet Galaxy
preco: '1100'
quantidade: '2'
```
**Saída JSON** 
```
[
    {
        "nome": "Iphone14",
        "preco": "7500",
        "quantidade": "2",
        "marca": "Apple",
        "cod_barra": "3123123712",
        "imposto": "135"
    },
    {
        "nome": "PS5",
        "preco": "3500",
        "quantidade": "2",
        "marca": "Sony",
        "cod_barra": "43436",
        "imposto": "250"
    },
    {
        "nome": "Camiseta Lacoste",
        "preco": "450",
        "quantidade": "2",
        "marca": "Lacoste",
        "cod_barra": "454543",
        "imposto": "100"
    },
    {
        "nome": "Tablet Galaxy",
        "preco": "1100",
        "quantidade": "2",
        "marca": "Samsung",
        "cod_barra": "12312",
        "imposto": "356"
    }
]
```

## **Critérios de aceitação:**
- O programa deve ler arquivos do tipo csv e escrever no formato específicado (JSON, XML, YAML)
- Criar repositório local e fazer push para o GitHub
- Utilizar algum método de contribuição estudado, como: GitFlow, Centralized Branch ou Featured Brach, com mensagens relevantes nos commits
- Adicionar um arquivo README.md com instruções de utilização do script

## **Bônus:**
- Gerar um arquivo PDF da nota fiscal
- Aceitar como parâmetro o nome do arquivo de base.


