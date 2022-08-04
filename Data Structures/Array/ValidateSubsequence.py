def isValidSubsequence(array, sequence):
    # Write your code here.
    output = True
    previous_index = -1

    i = 0
    while i < len(sequence):
        if sequence[i] not in array:
            output = False
            return output
        else:
            if previous_index == 0:
                previous_index = array.index(sequence[i])
                array.pop(array.index(sequence[i]))
            else:
                if previous_index > array.index(sequence[i]):
                    output = False
                    return output
                else:
                    previous_index = array.index(sequence[i])
                    array.pop(array.index(sequence[i]))

        i += 1
    return output