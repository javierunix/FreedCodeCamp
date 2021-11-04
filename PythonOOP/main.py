import csv

class Item:
	all_items = []
	pay_rate = 0.8 # the pay rate after 20% discount

	def __init__(self, name: str, price: float, quantity = 0):
		# run validations to received arguments
		assert price >= 0, f"Price {price} is not greater or equal than zero!"
		assert quantity >= 0, f"Quantity {quantity} is not greater or equal than zero!"

		# assign to self object
		self.name = name
		self.price = price
		self.quantity = quantity

		# actions to execute
		Item.all_items.append(self)

	@classmethod
	def instantiate_from_csv(cls):
		with open('items.csv', 'r') as f:
			reader = csv.DictReader(f)
			items = list(reader)

		for item in items:
			Item(
				name = item.get('name'),
				price = float(item.get('price')),
				quantity = int(item.get('quantity'))	
			)
	@staticmethod
	def is_int(num):
		# we are going to count out the decimals that are dot zero
		# i.e: 10.0, 5.0,...
		if isinstance(num, float):
			return num.is_integer()
		elif isinstance(num, int):
			return True
		else:
			return False

	def __repr__(self):
		return f"Item('{self.name}', {self.price}, {self.quantity})"

	def calculate_total_price(self):
		return self.quantity * self.price

	def apply_discount(self):
		self.price = self.pay_rate * self.price
		return self.price

