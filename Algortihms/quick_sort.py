def quick_sort(array, first, last):
    if first < last:
        split = partition(array, first, last)
        partition(array, first, split - 1)
        partition(array, split + 1, last)

    return array


def partition(array, first, last):
    pivot = array[first]
    l = first + 1
    r = last
    control = True

    while control:

        while l <= r and pivot >= array[l]:
            l += 1

        while r >= l and pivot <= array[r]:
            r -= 1

        if r < l:
            control = False

        else:
            array[l], array[r] = array[r], array[l]

    array[first], array[r] = array[r], array[first]

    return r
