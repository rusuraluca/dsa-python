def get_median(ll, ll2, n):
    i = j = 0
    m1 = m2 = -1
    count = 0
    while count < n + 1:
        count += 1
        if i == n:
            m1 = m2
            m2 = ll2[0]
            break
        elif j == n:
            m1 = m2
            m2 = ll[0]
            break
        if ll[i] <= ll2[j]:
            m1 = m2
            m2 = ll[i]
            i += 1
        else:
            m1 = m2
            m2 = ll2[j]
            j += 1
    return (m1 + m2) / 2


ll = [1, 12, 15, 26, 38]
ll2 = [2, 13, 17, 30, 45]
n1 = len(ll)
n2 = len(ll2)
print(get_median(ll, ll2, n1))
