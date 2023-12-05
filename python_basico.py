# Variáveis
nome = "João"
idade = 30
salario = 3000.50
ativo = True

# Condicionais
if idade >= 18:
    print(f"{nome} é maior de idade.")
else:
    print(f"{nome} é menor de idade.")

# Loops
for i in range(5):
    print(f"Contagem: {i}")

# Listas
cores = ["vermelho", "verde", "azul"]
print("Cores disponíveis:")
for cor in cores:
    print(cor)

# Dicionários
pessoa = {
    "nome": "Maria",
    "idade": 25,
    "cidade": "São Paulo"
}
print(f"{pessoa['nome']} tem {pessoa['idade']} anos e mora em {pessoa['cidade']}.")

# Arrays (usando a biblioteca NumPy)
import numpy as np

valores = np.array([1, 2, 3, 4, 5])
print("Valores do array:", valores)

# Exemplo de loop em um array
for valor in valores:
    print("Valor:", valor)
