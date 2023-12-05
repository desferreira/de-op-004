
# Conteúdo Programático

## Aula 1: Conceitos de Sistemas de Versionamento de Código

- Introdução aos sistemas de versionamento de código.
- Importância do versionamento de código em desenvolvimento de software.
- Vantagens de utilizar um sistema de versionamento.
- Compreensão de repositórios, controle de versões e histórico de alterações.

links: 
- https://blog.somostera.com/data-science/versionamento
- https://blog.betrybe.com/desenvolvimento-web/versionamento-software-codigo/
## Aula 2: Versionamento básico com Git

- Introdução ao Git: o que é, por que é amplamente utilizado.
- Instalação e configuração do Git.
- Inicialização de um repositório Git.
- Comandos básicos: git add, git commit, git status, git log, etc.
- Gerenciamento de branches locais.

links:
- https://kenzie.com.br/blog/o-que-e-git/
- https://blog.betrybe.com/git/

## Aula 3: Estratégias para resolução de conflitos e mesclando trabalho de outros usuários

- Compreensão de conflitos em Git.
- Resolução de conflitos manualmente.
- Fusão de branches e mesclagem de trabalho de outros usuários.
- Uso de ferramentas de comparação e resolução.

links:
- https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-using-the-command-line?platform=mac
- https://docs.github.com/pt/pull-requests/collaborating-with-pull-requests/addressing-merge-conflicts/resolving-a-merge-conflict-on-github

## Aula 4: Modelos tradicionais de Fluxo de Trabalho colaborativo usando Git

- Workflow centralizado (Centralized Workflow).
- Workflow baseado em branches (Feature Branch Workflow).
- Workflow Gitflow para gerenciar branches.
- Boas práticas para colaboração em equipe.

links:
- https://medium.com/jamalsoliva/git-workflows-centralized-featured-branch-and-git-flow-52ebb4efd3db

## Aula 5: Leitura e geração de arquivos XML

- Introdução ao formato XML.
- Leitura de arquivos XML em diferentes linguagens de programação.
- Geração e criação de arquivos XML.
- Manipulação de elementos e atributos XML.

## Aula 6: Leitura e geração de arquivos JSON

- Introdução ao formato JSON.
- Leitura de arquivos JSON em diferentes linguagens de programação.
- Geração e criação de arquivos JSON.
- Manipulação de objetos e arrays JSON.

## Aula 7: Leitura e geração de arquivos YAML

- Introdução ao formato YAML.
- Leitura de arquivos YAML em diferentes linguagens de programação.
- Geração e criação de arquivos YAML.
- Estrutura hierárquica em YAML.

## Aula 8: Projeto prático e conclusão

- Desenvolvimento de um projeto prático que envolve o uso de Git, XML, JSON e YAML.
- Revisão dos conceitos aprendidos.
- Melhores práticas para gerenciar código e dados.
- Encerramento do curso e recursos adicionais para aprofundamento.

## Projeto
- https://docs.google.com/document/d/1Bk09dXUtpsLQrrEg0OlvvWFQj2mG57L9xpxX2h8I9WE/edit?usp=sharing
- video: https://www.youtube.com/watch?v=Y8wCfxUm2KI&list=WL&index=2&t=3s
- jupyter online: https://jupyter.org/try-jupyter/retro/notebooks/?path=Untitled.ipynb

# Como utilizar os scripts

Antes de usar os scripts, existe um arquivo `requirements.txt` que tem todas as dependências, basta você instalar todas no seu ambiente com `pip install -r requirements.txt` e seu ambiente estará preparado para testar os scripts.

- Para gerar e ler jsons, use o: `exemplo_aula_json.py`
- Para gerar e ler yamls, use o: `exemplo_aula_yaml.py`
- Para gerar e ler xmls, use o: `exemplo_aula_xml.py`
- Para gerar gráficos direto com o python, sem o jupyter notebook, use o: `script.com_graficos.py`

A forma de utilizar eles é simples, basta executar a chamada do python com: `python exemplo_aula_json.py` e isto vai fazer duas coisas:
1. Gerar um arquivo exemplo.json na pasta `exemplos_arquivos`
2. Printar na tela o conteúdo do arquivo `exemplos_arquivos/squirtle.json`
