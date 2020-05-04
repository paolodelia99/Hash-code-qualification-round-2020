a = [(1, 2, 3, 4)]

b = [4, 5, 6]

a1 = set(list(sum(a, ())))
b = set(b)

c = b.difference(a1)

print(c)