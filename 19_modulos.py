import sys

print(sys.path)

contar = [1,2,3,4,5]

contar_new = list(map(lambda i: i + 1,contar))
print(contar_new)