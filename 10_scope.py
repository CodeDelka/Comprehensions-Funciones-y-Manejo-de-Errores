price = 100 #alcance global

def increment():
    result = 200 #alcance local
    print(result)
    return(result)

print(price)
increment()

