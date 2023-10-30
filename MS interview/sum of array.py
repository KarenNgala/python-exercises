# output an array with length N
# sum of array elements should equal zero
# negative integers are allowed
# many integer combinations are possible for single input

def sum_of_array(N):
    array = []

    if N%2 != 0:
        array.append(0)

    for i in range(1, N//2+1):
        array.append(i)
        array.append(-i)

    print(array)


sum_of_array(9)