def merge(array):
    if len(array) > 1:

        mid = len(array) // 2
        l_array = array[:mid]
        r_array = array[mid:]

        merge(l_array)
        merge(r_array)

        i = j = k = 0

        while i < len(r_array) and j < len(l_array):

            if r_array[i] < l_array[j]:

                array[k] = r_array[i]
                i += 1
            else:

                array[k] = l_array[j]
                j += 1

            k += 1

        while i < len(r_array):
            array[k] = r_array[i]
            i += 1
            k += 1

        while j < len(l_array):
            array[k] = l_array[j]
            j += 1
            k += 1

    return array
