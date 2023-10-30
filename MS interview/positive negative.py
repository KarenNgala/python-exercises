# Find largest positive and negative number in array

def longestNum(arr):
    arr2 = []
    for num in arr:
        if num in arr and -num in arr:
            arr2.append(num)
            return max(arr2) 
        return 'NO'


arr =[3, 2, -2, 5, -3]
print(longestNum(arr))