def merge_sort(lista):
    if len(lista) <= 1:  # Caso base: lista com 1 ou 0 elementos
        return lista
    
    # Dividir a lista ao meio
    meio = len(lista) // 2
    esquerda = merge_sort(lista[:meio])  # Ordena a metade esquerda
    direita = merge_sort(lista[meio:])   # Ordena a metade direita
    
    # Mesclar as duas metades ordenadas
    return merge(esquerda, direita)

def merge(esquerda, direita):
    resultado = []
    i = j = 0
    
    # Mescla as duas listas enquanto elas tiverem elementos
    while i < len(esquerda) and j < len(direita):
        if esquerda[i] < direita[j]:
            resultado.append(esquerda[i])
            i += 1
        else:
            resultado.append(direita[j])
            j += 1
    
    # Adiciona os elementos restantes de cada lista, se houver
    resultado.extend(esquerda[i:])
    resultado.extend(direita[j:])
    
    return resultado

lista = [38, 27, 43, 3, 9, 82, 10]
lista_ordenada = merge_sort(lista)
print(lista_ordenada)  # Saída: [3, 9, 10, 27, 38, 43, 82]
