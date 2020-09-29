def rec_search(l, x):
    mid = int(len(l) / 2)

    if len(l) == 1:
        return False

    if l[mid] == x:
        return True

    else:

        if x < l[mid]:
            return search(l[:mid], x)

        else:
            return search(l[mid:], x)


def search(l, n):
    _min, _max = 0, len(l) - 1

    while _min <= _max:

        mid = (_min + _max) // 2

        if l[mid] > n:
            _max = mid - 1

        elif l[mid] < n:
            _min = mid + 1

        else:
            return mid

    return -1
