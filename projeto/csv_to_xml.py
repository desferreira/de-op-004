import csv
import xml.etree.ElementTree as ET


def converterParaXml(): 
# Substitua 'seuarquivo.csv' pelo caminho para o seu arquivo CSV
    nome_do_arquivo = 'produtos.csv'
    # Use o método 'with' para abrir o arquivo CSV
    with open(nome_do_arquivo, mode='r') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        
        # Crie o elemento raiz do XML
        raiz = ET.Element("listaDeProdutos")

        # Iterar pelas linhas do arquivo CSV e criar elementos XML
        for i, linha in enumerate(leitor_csv):
            if i == 0:
                headers = linha
                print(f'os headers são {headers}')
            produto = ET.Element("produto")
            raiz.append(produto)

            for i, valor in enumerate(linha):
                ET.SubElement(produto, headers[i]).text = valor

        # Crie uma árvore XML
        arvore = ET.ElementTree(raiz)

        # Salve o XML em um arquivo
        nome_do_xml = "produtos.xml"
        arvore.write(nome_do_xml)

        print("Arquivo XML gerado com sucesso:", nome_do_xml)
