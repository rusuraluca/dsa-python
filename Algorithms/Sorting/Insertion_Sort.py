def insertion(ll: list):
    for i in range(1, len(ll)):
        key = ll[i]
        j = i - 1
        while j >= 0 and key < ll[j]:
            ll[j + 1] = ll[j]
            j -= 1
        ll[j + 1] = key
    return ll


ll = [1, 3, 4, 7, 5, 9]
print(insertion(ll))

