import csv


class Item:
	all = []
	pay_rate = 0.8

	def __init__(self, name: str, price: float, quantity=0):
		# run validations to received arguments
		assert price >= 0, f"Price {price} is not greater or equal than zero!"
		assert quantity >= 0, f"Quantity {quantity} is not greater or equal than zero!"

		# assign to self object
		self.__name = name
		self.__price = price
		self.quantity = quantity

		# actions to execute
		Item.all.append(self)

	@property
	def price(self):
		return self.__price

	def apply_discount(self):
		self.__price = self.__price * self.pay_rate
		return self.__price

	def apply_increment(self, inc_rate):
		self.__price = self.__price + self.__price * inc_rate

	@property
	# property declarator = read-only atribute
	def name(self):
		return self.__name

	# setter method for the name atribute
	@name.setter
	def name(self, newname):
		if len(newname) > 10:
			raise Exception('The name is to long!')
		else:
			self.__name = newname

	@classmethod
	def instantiate_from_csv(cls):
		with open('items.csv', 'r') as f:
			reader = csv.DictReader(f)
			items = list(reader)

		for item in items:
			Item(
				name=item.get('name'),
				price=float(item.get('price')),
				quantity=int(item.get('quantity'))
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
		return f"{self.__class__.__name__}('{self.name}', {self.__price}, {self.quantity})"

	def calculate_total_price(self):
		return self.quantity * self.__price

