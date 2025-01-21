def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        if caractere in contagem:
            contagem[caractere] += 1
        else:
            contagem[caractere] = 1
    return contagem

print(contar_caracteres("banana"))