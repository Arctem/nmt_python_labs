def anadist(a, b):
    a = list(a)
    b = list(b)
    dist = 0
    while a:
        if a[0] in b:
            b.remove(a[0])
        else:
            dist += 1
        a.remove(a[0])
    dist += len(b)
    return dist

print(anadist(input(), input()))
        
