import yaml


def escrever_arquivo_yaml(caminho_arquivo):
    # Dados a serem escritos no arquivo YAML
    dados_yaml = {
        'pessoas': [
            {'nome': 'Lucas', 'idade': 30},
            {'nome': 'Maria', 'idade': 25}
        ]
    }

    with open(caminho_arquivo, 'w') as arquivo:
        # Escreve os dados no arquivo YAML
        yaml.dump(dados_yaml, arquivo, default_flow_style=False)

    print(f"Arquivo YAML '{caminho_arquivo}' criado com sucesso!")

def ler_arquivo_yaml(caminho_arquivo):
    # Abrir o arquivo YAML
    with open(caminho_arquivo, 'r') as arquivo:
        # Carregar os dados YAML como um objeto Python
        dados = yaml.load(arquivo, Loader=yaml.FullLoader)

    # Manipular os dados convertidos como um dicionário
    print(dados)


yaml_leitura = 'exemplos_arquivos/values.yaml'
yaml_escrita = 'exemplos_arquivos/exemplo.yaml'
ler_arquivo_yaml(yaml_leitura)
escrever_arquivo_yaml(yaml_escrita)
