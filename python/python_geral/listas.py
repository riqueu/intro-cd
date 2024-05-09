# Listas

primeira_lista = [1, 1.1, "um ponto um", ["F", "G", "V"], "Helouise"]
# print(primeira_lista)

#for elemento in primeira_lista:
#    print(elemento)

for coiso in primeira_lista[3]:
    print(coiso.lower())

print()

lista = ["E", "M", "A", "P"]
print(lista[::-1])

print()

lista = ["Marco Aurélio", "Zenão de Cítio", "Sêneca", "Epiteto", "Dilmar Listas"]
print(lista[-1])
print(lista[2:4])
del lista[4]
lista.extend(["Carlos Ivan", "C. Camacho"])
print(lista)
for cada_elemento in lista:
    print(cada_elemento)

print()

pares = [1, 3, 5, 7, 9]
for i in range(len(pares)):
    pares[i] += 1
print(pares)
del(pares[1:4])
print(pares)
# del, remove, pop, clear

print()

print(primeira_lista + lista)
print(primeira_lista * 2)

print()

frase = "adoro a emap"
print(frase[::-1])
text = "!~a-l4o8 4,9o1n5a2m"
print(text[::-2].upper())
for cada_letra in frase:
    print(cada_letra)
