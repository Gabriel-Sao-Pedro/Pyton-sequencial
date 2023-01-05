x = float(input("Digite a largura do terreno \n"))
y = float(input("Digite o comprimento do terreno \n"))
z = float(input("Digite o valor do metro quadrado \n"))

a = x * y
v = a * z

print("A area do terreno e {:.2f}".format(a))
print("O valor do terreno e {:.2f}".format(v))
