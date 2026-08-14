""""product = {'itemid': 1234, 'name': 'Widget', 'coloue': 'black'}

print(product['itemid'])
product['size'] = ['Small', 'Medium', 'Large']

print(product['size'][2])

print(product[0]['itemid'])

"""
products = [
    {'itemid': 1234, 'name': 'Widget', 'colour': 'black'},
    {'itemid': 1254, 'name': 'shirt', 'colour': 'red'},
    {'itemid': 1678, 'name': 'top', 'colour': 'pink'},
    {'itemid': 6789, 'name': 'shoe', 'colour': 'orange'}
]

for product in products:
    item = product['itemid']
    if item > 3455:
        print("bad")
    else:
        print("good")
