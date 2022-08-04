"""
countingSort(array, size)
  max <- find maximum element in the array
  initialize count array with all 0s

  for m <- 0 to size
    find the total count of each unique element and
    store the count at mth index in count array

  for n <- 1 to max
    find the cumulative sum and store it in a count array

  for m <- size down to 1
    restore the elements to the array
    decrease count of each element by 1

  return list
"""


def counting(ll: list) -> list:
    size = len(ll)
    output = [0] * size

    # Count array initialization
    count = [0] * 10

    # Storing the count of each element
    for m in range(0, size):
        count[ll[m]] += 1

    # Storing the cumulative count
    for m in range(1, 10):
        count[m] += count[m - 1]

    # Place the elements in output array after finding the index of each element of original array in count array
    m = size - 1
    while m >= 0:
        output[count[ll[m]] - 1] = ll[m]
        count[ll[m]] -= 1
        m -= 1

    for m in range(0, size):
        ll[m] = output[m]

    return ll


ll = [1, 3, 4, 7, 5, 9]
print(counting(ll))
