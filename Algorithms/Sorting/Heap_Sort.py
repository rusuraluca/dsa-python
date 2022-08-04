def heap(ll: list) -> list:
    def swap(i, j):
        ll[i], ll[j] = ll[j], ll[i]

    def heapify(end, i):
        l = 2 * i + 1
        r = 2 * (i + 1)
        max = i
        if l < end and ll[i] < ll[l]:
            max = l
        if r < end and ll[max] < ll[r]:
            max = r
        if max != i:
            swap(i, max)
            heapify(end, max)

    def heap_sort(ll):
        end = len(ll)
        start = end // 2 - 1
        for i in range(start, -1, -1):
            heapify(end, i)
        for i in range(end - 1, 0, -1):
            swap(i, 0)
            heapify(i, 0)
        return ll

    return heap_sort(ll)


l = [1, 3, 4, 7, 5, 9]
print(heap(l))
