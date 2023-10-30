def solve(s):
    str_arr = []
    for i in range(len(s)-1, -1, -1):
        for j in range(len(str_arr)):
            str_arr.append(s[i]+str_arr[j])
        str_arr.append(s[i])
    return str_arr


s = 'jetcob'
print(solve(s))