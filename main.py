class Item:
	def calculate_total_price(self):
		return self.quantity * self.price

item1 = Item()
item2 = Item()

item1.name = 'Phone'
item1.price = 100
item1.quantity = 5
print(item1.calculate_total_price())

item2.name = 'Laptop'
item2.price = 1000
item2.quantity = 3
print(item2.calculate_total_price())
