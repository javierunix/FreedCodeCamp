class Item:

	def __init__(self, name):
		print(f"An instance created: {name}")
		self.name = name

	def calculate_total_price(self, quantity, price):
		return quantity * price

item1 = Item('Phone')
item2 = Item('Laptop')

item1.price = 100
item1.quantity = 5

item2.price = 1000
item2.quantity = 3

print(item1.name)
print(item2.name)