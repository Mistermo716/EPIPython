def hIndex(citations):
    citations.sort()
    n = len(citations)

    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i
    return 0


c = [1, 3, 5, 6, 2, 3, 4, 5, 6, 3, 2, 4]

test = hIndex(c)
print(test)
