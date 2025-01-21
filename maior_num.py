numeros = []

while True:
    num = float(input("Digite um número: "))
    if num >= 0:
        numeros.append(num)
    else:
        break

maior_num = max(numeros)

print("\n", numeros)
print(f"\nO maior número dessa lista é {maior_num}")