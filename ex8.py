carros = ['fusca', 'corcel', 'fiat 147', 'marea']
print(carros[0])
print("monstrando todos os veiculos")

carros.append("opala")

novoCarro = input("Digite um novo veículo: ")
carros.append(novoCarro)

carros.sort()

x = 1

for carro in carros:
    print ("o {0}° carro é o {1}".format(x, carro))
    x += 1
