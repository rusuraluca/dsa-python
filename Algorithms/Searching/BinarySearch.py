def binary_search(lo, hi, condition):
    """
    @def: Search a sorted list to find an elements of a certain condition
		@return: bool
				 => true,  if condition is true
                 => false, otherwise
    """
    while lo <= hi:
        mid = (lo + hi) // 2
        result = condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid - 1
        else:
            lo = mid + 1
    return -1


def binary_search_recursive(elems: list, target: int) -> bool:
    """
    @def: Search a sorted list to find a target integer
		@return: bool
				 => true,  if target in array
				 => false, otherwise
    """
    if len(elems) < 1:
        return False

    if len(elems) == 1:
        return elems[0] == target

    mid = len(elems) // 2

    if elems[mid] < target:
        return binary_search_recursive(elems[mid:], target)

    elif elems[mid] > target:
        return binary_search_recursive(elems[:mid], target)

    else:
        return True


def binary_search_iterative(elems: list, target: int) -> bool:
    """
    @def: Search a sorted list to find a target integer
		@return: bool
				 => true,  if target in array
				 => false, otherwise
    """
    if len(elems) < 1:
        return False

    if len(elems) == 1:
        return elems[0] == target

    st, end, mid_pos, mid = 0, len(elems) - 1, 0, 0

    while (st <= end):
        mid_pos = (st + end) // 2

        if elems[mid] == target:
            return True

        elif elems[mid] > target:
            end = mid - 1

        elif elems[mid] < target:
            st = mid + 1

    return False
