def are_all_members_same(lista):
    if lista.count(lista[0]) == len(lista):
        return True
    else:
        return False

print(are_all_members_same([2, 2, 2, 2]))