from math import sqrt

c = float(input("Digite o comprimento da base do retangulo \n"))
h = float(input("Digite o comprimento da altura do retangulo \n"))

a = c * h
p = 2*(c) + 2*(h)
d = sqrt((c)**2 + (h)**2)
print("Area do quadrado {:.4f}".format(a))
print("Perimetro do quadrado {:.4f}".format(p))
print("Diagonal do quadrado {:.4f}".format(d))
