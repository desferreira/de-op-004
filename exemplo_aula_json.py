import requests
import json

def ler_json_da_web(url):
    x = requests.get('https://api.thecatapi.com/v1/images/search?limit=10')

    for element in x.json():
        print(element['id'])

def ler_arquivo_json(caminho_arquivo):
    with open(caminho_arquivo, 'r') as arquivo:
        # Carrega o conteúdo do arquivo JSON
        dados_json = json.load(arquivo)

        # Aqui, você pode acessar os dados do JSON conforme necessário
        print("Dados do JSON:")
        print(json.dumps(dados_json, indent=2))

def escrever_arquivo_json(caminho_arquivo):
    # Dados a serem escritos no arquivo JSON
    dados_json = {
        "pessoas": [
            {"nome": "Mario", "idade": 30},
            {"nome": "Maria", "idade": 25}
        ]
    }
    with open(caminho_arquivo, 'w') as arquivo:
        # Escreve os dados no arquivo JSON
        json.dump(dados_json, arquivo, indent=2)

    print(f"Arquivo JSON '{caminho_arquivo}' criado com sucesso!")

json_leitura = 'exemplos_arquivos/squirtle.json'
json_escrita = 'exemplos_arquivos/exemplo.json'
ler_arquivo_json(json_leitura)
escrever_arquivo_json(json_escrita)
