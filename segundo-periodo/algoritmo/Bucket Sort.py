def bucket_sort(lista):
    num_buckets = 10
    buckets = []
    for _ in range(num_buckets):
        buckets.append([])

    maior = max(lista)

    for e in lista:
        i = int(e * num_buckets / (maior + 1))
        buckets[i].append(e)

    lista_ordenada = []
    for bucket in buckets:
        lista_ordenada.extend(sorted(bucket))

    return lista_ordenada

lista = [0.23, 0.34, 0.45, 0.12, 0.78, 0.56]
result = bucket_sort(lista)
print(result)