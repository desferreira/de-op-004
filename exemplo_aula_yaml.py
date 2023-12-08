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
        yaml.dump(dados_yaml, arquivo, sort_keys=True)

    print(f"Arquivo YAML '{caminho_arquivo}' criado com sucesso!")

def ler_arquivo_yaml(caminho_arquivo):
    # Abrir o arquivo YAML
    with open(caminho_arquivo, 'r') as arquivo:
        # Carregar os dados YAML como um objeto Python
        dados = yaml.load(arquivo, Loader=yaml.FullLoader)

    # Manipular os dados convertidos como um dicionário
    return dados


def adicionar_produto(caminho_arquivo, nome, preco, quantidade): 
    conteudoAtual = ler_arquivo_yaml(caminho_arquivo)
    conteudoAtual["pessoas"].append({"nome": nome, "preco": preco, "quantidade": quantidade})
    with open(caminho_arquivo, 'a') as arquivo:
    # Escreve os dados no arquivo YAML
        yaml.dump(conteudoAtual, arquivo, sort_keys=True)

yaml_leitura = 'exemplos_arquivos/values.yaml'
yaml_escrita = 'exemplos_arquivos/exemplo.yaml'
ler_arquivo_yaml(yaml_leitura)
escrever_arquivo_yaml(yaml_escrita)
adicionar_produto(yaml_escrita, "diego", 321312312, 3)
