lista=[1,23,2,3,34,23,0,0,0,0,0,0,0]
lista1 = sorted(lista)
print(lista)
määrä0 = lista1.count(0)
del lista1[0:määrä0]
viimeinen = max(lista1)
eniten = max(lista1, key=lista1.count)
print(määrä0)
print(lista1)
print(viimeinen)
print(eniten)