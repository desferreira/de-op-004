import csv
import json

def converterParaJson(): 
    # Ler o arquivo CSV e armazenar os dados em uma lista de dicionários
    csv_file = 'produtos.csv'
    json_file = 'produtos.json'

    data = []
    with open(csv_file, 'r') as csvf:
        csvreader = csv.DictReader(csvf)
        for row in csvreader:
            data.append(row)

    # Escrever os dados em um arquivo JSON
    with open(json_file, 'w') as jsonf:
        json.dump(data, jsonf, indent=4)

    print(f'Arquivo CSV "{csv_file}" foi convertido para JSON em "{json_file}"')
