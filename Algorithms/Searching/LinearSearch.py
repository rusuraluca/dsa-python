def linear_search(elems: list, target: int) -> bool:
    """
    @def: Search an unordered list to find a target integer
	@return: bool
	         => true,  if target in array
             => false, otherwise
    """
    for elem in elems:
        if elem == target:
            return True

    return False
