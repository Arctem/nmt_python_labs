def anadist(a, b):
    a = list(a)
    b = list(b)
    dist = 0
    for i in a:
        if i in b:
            b.remove(i)
        else:
            dist += 1
    dist += len(b)
    return dist

print(anadist(input(), input()))
        
