"""
quick_sort(ll, leftmostIndex, rightmostIndex)
  if (leftmostIndex < rightmostIndex)
    pivotIndex <- partition(ll,leftmostIndex, rightmostIndex)
    quickSort(ll, leftmostIndex, pivotIndex - 1)
    quickSort(ll, pivotIndex, rightmostIndex)

partition(ll, leftmostIndex, rightmostIndex)
  set rightmostIndex as pivotIndex
  storeIndex <- leftmostIndex - 1
  for i <- leftmostIndex + 1 to rightmostIndex
  if element[i] < pivotElement
    swap element[i] and element[storeIndex]
    storeIndex++
  swap pivotElement and element[storeIndex+1]
return storeIndex + 1
"""


# method
def quick(ll):
    
    # function to find the partition position
    def partition(ll, low, high):

        # choose the rightmost element as pivot
        pivot = ll[high]

        # pointer for greater element
        i = low - 1

        # traverse through all elements
        # compare each element with pivot
        for j in range(low, high):
            if ll[j] <= pivot:
                # if element smaller than pivot is found
                # swap it with the greater element pointed by i
                i = i + 1

                # swapping element at i with element at j
                (ll[i], ll[j]) = (ll[j], ll[i])

        # swap the pivot element with the greater element specified by i
        (ll[i + 1], ll[high]) = (ll[high], ll[i + 1])

        # return the position from where partition is done
        return i + 1

    # function to perform quicksort
    def quick_sort(ll, low, high):
        if low < high:
            # find pivot element such that
            # element smaller than pivot are on the left
            # element greater than pivot are on the right
            pi = partition(ll, low, high)

            # recursive call on the left of pivot
            quick_sort(ll, low, pi - 1)

            # recursive call on the right of pivot
            quick_sort(ll, pi + 1, high)

    low = 0
    high = len(ll) - 1
    quick_sort(ll, low, high)
    return ll


ll = [1, 3, 4, 7, 5, 9]
print(quick(ll))

