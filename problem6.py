n1 = list(range(1,101))
s = lambda a: a**2
n2 = list(s(i) for i in n1)
n1 = sum(n1)**2
n2 = sum(n2)
print(abs(n1 - n2))