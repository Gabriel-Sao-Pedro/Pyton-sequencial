p = float(input("Valor do produto: "))
u = int(input("Quantidade do produto: "))
v = float(input("Valor recebido: "))

x = p * u
t = v - x

print("TROCO = {:.2f}".format(t))
