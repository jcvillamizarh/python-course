# Función map con diccionario de datos

items = [{
  'product': 'camisa',
  'price': 100,
}, {
  'product': 'patantalon',
  'price': 200
}, 
{
  'product': 'pantalon',
  'price': 300
}]

prices = list(map(lambda item: item['price'], items))
print(prices)

def add_taxes(item):
  item['taxes'] = item['price'] * .19
  return item

taxes = list(map(add_taxes, items))
print(taxes)
