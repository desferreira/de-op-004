import csv
import yaml

def converterParaYAML(): 
    # Ler o arquivo CSV e armazenar os dados em uma lista de dicionários
    csv_file = 'produtos.csv'
    yaml_file = 'produtos.yaml'

    data = []
    with open(csv_file, 'r') as csvf:
        csvreader = csv.DictReader(csvf)
        for row in csvreader:
            data.append(row)

    # Escrever os dados em um arquivo YAML
    with open(yaml_file, 'w') as yamlf:
        yaml.dump(data, yamlf, default_flow_style=False)

    print(f'Arquivo CSV "{csv_file}" foi convertido para YAML em "{yaml_file}"')
