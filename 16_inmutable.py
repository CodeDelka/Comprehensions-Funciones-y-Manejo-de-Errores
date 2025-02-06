items = [ 
    { 'product': 'camisa', 'price': 200 },
    {'product': 'pantalon',  'price': 400 },
    {'product': 'zapatos','price': 800 }
]
##se copia la lista original para que no sufra modificaciones
def add_taxes(item):
    new_item = item.copy()
    new_item['taxes'] = item['price'] * .19 
    return new_item

new_items = list(map(add_taxes, items))
print('new list')
print(new_items)

print('old list')
print(items)

