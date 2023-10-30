# x = 5
# y = x + 3
# x = x - 1
# z = 10
# x = x + z
# # print('x: {}, y: {}, z: {}'.format(x, y, z))

# # print(14//4, 14%4, 14.0/4)

# d = dict()
# d['left'] = '<<'
# d['right'] = '>>'
# # print('{left} and {right} or {right} and {left}'.format(**d))

# a = [20, 'Chelsea']
# b = (10, 'Manchester')
# a[0] = 30
# # print(a[0], b[0])

# items = ['sugar', 'salt', 'milk', 'bread']
# price = [120, 20, 55, 55]
# shopping = dict(zip(items, price))
# print(shopping)
# # print(**shopping)
import numpy as np

def even(n):
    array = np.random.randint(10, size=n)
    count = 0
    for i in array:
        if i%2==0:
            count = count+1
    return count, array

print(even(4))