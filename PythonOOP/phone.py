from item import Item


class Phone(Item):
	pay_rate = 0.5

	def __init__(self, name: str, price: float, quantity=0, broken_phones=0):
		# Call to super function to have access to all attributes / methods
		super().__init__(
			name, price, quantity
		)

		# run validation for received parameters
		assert broken_phones >= 0, f"Broken phones {broken_phones} is not greater or equal than zero!"

		# assign to self object
		self.broken_phones = broken_phones

