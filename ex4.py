import os

os.system("cls")
print("------------------------------------------------")

nome = input("Digite o nome:\n")
nota1 = float(input("Digite a nota 1:\n"))
nota2 = float(input("Digite a nota 2:\n"))

media = (nota1 + nota2)/2

#verificar se vai passar, ficar de exame ou reprovar
if (media >= 7):
    print("Sua nota foi {0:.2f} e você passou" .format(media))

elif(media >=4):
    print("Sua nota foi {0:.2f}, e você ficou de exame" .format(media))
    
else:
    print("Sua nota foi de {0:.2f} e você reprovou" .format(media))


