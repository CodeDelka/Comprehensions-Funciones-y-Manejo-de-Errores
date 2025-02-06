#funcion sin lambda
def increment(x): 
    return x + 1

#funcion con lambda
increment_v2 = lambda x : x + 1

#funcion dentro de una funcion sin lambda
def high_ord_func(x, func):
    return x + func(x)

#funcion dentro de una funcion con lambda
high_ord_func_v2 = lambda x, func : x + func(x)

#print con lambda
result = high_ord_func_v2(10, increment_v2)
print(result)