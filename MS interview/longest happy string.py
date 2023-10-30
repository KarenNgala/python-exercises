# print longest string containing letters a, b, c
# function accepts integers denoting how max no. of each letter the string can have. A letter 'a', B letter 'b'...
# string can have a maximum of 2 repeating characters 'aaacd' is incorrect
# output empty string if no possibility of unique string
# there are many correct solutions for one input combination
# input integers are >0 and <100

def longest_happy_string(A, B, C):
    numbers = [A, B, C]
    res = ""

    
    if A <= 1 or B <= 1 or C <= 1:
        res = res + 'a'*A
        res = res + 'b'*B
        res = res + 'c'*C
    if A > 1 or B > 1 or C > 1:
        res = res + 'a'*2 
        res = res + 'b'*2 
        res = res + 'c'*2 
        A-=2
        B-=2
        C-=2

    if 'a'*3 not in res and 'b'*3 not in res and'c'*3 not in res:
        return res 


print(longest_happy_string(6,1,1))