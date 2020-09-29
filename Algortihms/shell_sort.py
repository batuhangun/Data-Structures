def shell(array):
    lenght = len(array)
    gap = int(lenght // 2)

    while gap > 0:

        for i in range(gap, lenght):

            curr = array[i]
            index = i
            while index >= gap and array[index - gap] > curr:
                array[index] = array[index - gap]
                index -= gap

            array[index] = curr

        gap //= 2
        gap = int(gap)
    return array
