import functools
#
#
numbers = [1,2,3,4]

def accum(i, x):
    print('Item => ',i)
    print('counter => ',x)
    return(i + x)

result = functools.reduce(accum, numbers )


print(result)