a = [1,2,3,2,1,5,6,5,5,5]

seen = set()
dupes = []

for x in a:
    if x in seen:
        dupes.append(x)
    else:
        seen.add(x)

print(dupes)

from calendar import c


a = ['a', 'b', 'c']
b = a
c = a[:]

b[0] = 'd'
c[1] = 'e'
sum = 0

x = list(set(a) & set(b) & set(c))
if 'd' in x:
    sum = sum +1
if 'e' in x:
    sum = sum + 10

print(c)

def maxSubArray(nums):
    
    dp = [0 for i in range(len(nums))]
    dp[0] = nums[0]
    for i in range(0,len(nums)):
        dp[i] = max(dp[i-1]+nums[i],nums[i])
    #print(dp)
    print(max(dp))


nums = [-2,1,-3,7,-2,2,1,-5,4]
maxSubArray(nums)
