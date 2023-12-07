# testando a classe Veículo

from Veiculo import Veiculo

minhaCaranga = Veiculo('Fiat', '147', 'Amarelo', 0)

# Exibindo a minha caranga
print('\n\t\t\t -- Minha Caranga --\n')
print(minhaCaranga)

# Acelerando a minha caranga
for i in range(0, 200):
    minhaCaranga.acelerar()

# Exibindo a minha caranga acelerada
print('\n\t\t\t -- Minha Caranga Acelerada --\n')
print(minhaCaranga)

for i in range(0, 200):
    minhaCaranga.frear()

# Exibindo a minha caranga freada
print('\n\t\t\t -- Minha Caranga Freada --\n')
print(minhaCaranga)
