def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    non_zeros = []
    zeros = []
    tiles = []
    actual_is_tiled = False

    for number in line:
        if number != 0:
            non_zeros.append(number)
        else:
            zeros.append(0)

    for index in range(len(non_zeros)):
        actual = non_zeros[index]

        if actual_is_tiled:
            zeros.append(0)
            actual_is_tiled = False
        
        elif index < len(non_zeros) - 1:
            next_num=non_zeros[index + 1]
            if actual != next_num:
                tiles.append(actual)
            else:
                tiles.append(actual + next_num)
                actual_is_tiled = True
        else:
            tiles.append(actual)

    return tiles + zeros

if __name__ == "__main__":
    print(merge([2,2,2,2]))
