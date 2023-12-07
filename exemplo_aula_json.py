import requests
import json

def ler_json_da_web(url):
    # Faz um pedido à API
    x = requests.get(url)
    # Converte o valor em binário para formato "json" entendível
    output = json.loads(x.content)
    # Percorre o output e lista o conteúdo
    if not isinstance(output, list):
        output = [output]
    for element in output:
        print(f'A url do gato é: {element["url"]}')
        foto_gato = requests.get(element["url"])
        with open("cat.jpg", 'wb') as f:
            f.write(foto_gato.content)

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


# Cat API - https://developers.thecatapi.com/view-account/ylX4blBYT9FaoVd6OhvR?report=bOoHBz-8t
catApi = 'https://api.thecatapi.com/v1/images/search?limit=10'
# https://github.com/15Dkatz/official_joke_api
jokeApi = 'https://official-joke-api.appspot.com/random_joke'
json_leitura = 'exemplos_arquivos/squirtle.json'
json_escrita = 'exemplos_arquivos/exemplo.json'
# ler_arquivo_json(json_leitura)
# escrever_arquivo_json(json_escrita)
ler_json_da_web(catApi)
