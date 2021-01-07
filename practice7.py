L = list(range(2, 30))
for i in L:
    for j in L:
        if j != i and j % i == 0:
            L.remove(j)


print(L)
    
