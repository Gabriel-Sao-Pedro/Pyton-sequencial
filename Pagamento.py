n = str(input("Nome: "))
v = float(input("Valor por hora: "))
h = float(input("Horas trabalhadas: "))

s = v * h

print("O pagamento para {} deve ser {:.2f}".format(n, s))
