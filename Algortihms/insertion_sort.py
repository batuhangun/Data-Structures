def insertion_sort(array):
    for i in range(1, len(array)):

        index = i
        curr = array[i]

        while index > 0 and array[index - 1] > curr:
            array[index] = array[index - 1]
            index -= 1

        array[index] = curr

    return array
