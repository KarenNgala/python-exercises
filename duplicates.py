# you can write to stdout for debugging purposes, e.g.
from random import seed


def duplicates(arr, x):
    count = 0
    seen = set()
    duplicates = {}
    for num in arr:
        if num in seen:
            count = count + 1
            duplicates.update({num:count})
        else:
            seen.add(num)

    for no in duplicates.values():
        if no > x:
            print(duplicates.keys())
    
    print(seen[7])


A = [0, 1, 2, 2, 3, 3, 3, 5, 5, 5, 5, 5, 5, 7, 8, 8, 10]
X = 3

duplicates(A, X)