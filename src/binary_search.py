def binary_search(*, ls: list[int], num: int) -> int:
    ls.sort()

    i, j = 0, len(ls) - 1

    while i < j:
        middle = (i + j) // 2
        if num < ls[middle]:
            j = middle - 1
        elif num > ls[middle]:
            i = middle + 1
        else:
            return middle
