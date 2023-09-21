# Inmutabilidad con map

items = [{
  'product': 'camisa',
  'price': 100,
}, {
  'product': 'patantalon',
  'price': 200
}, {
  'product': 'pantalon',
  'price': 300
}]

prices = list(map(lambda item: item['price'], items))
print(prices)


def add_taxes(item):
  new_item = item.copy()
  new_item['taxes'] = new_item['price'] * .19
  return new_item

taxes = list(map(add_taxes, items))
print(taxes)
print(items)
