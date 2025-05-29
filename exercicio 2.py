numero = int(input("Digite um número de cinco dígitos: "))


di1 = numero // 10000
di2 = (numero // 1000) % 10
di3 = (numero // 100) % 10
di4 = (numero // 10) % 10
di5 = numero % 10


print(di1)
print(di2)
print(di3)
print(di4)
print(di5)