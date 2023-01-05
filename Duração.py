x = float(input("Digite a duração em segundos: "))

h = x // 3600
mh = x % 3600
m = mh // 60
s = x % 60

print("{:.0f} : {:.0f} : {:.0f}".format(h, m, s))
