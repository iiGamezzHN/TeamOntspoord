class Station():
	"""docstring for ClassName"""


	def __init__(self,name,label,importance,location,neighbours):
		self.name = name
		self.label = label
		self.importance = importance
		self.location = location
		self.neighbours = neighbours


	def information(self):
		return '{} {} {} {} {}'.format(self.name, self.label, self.importance, self.location, self.neighbours)


	def update_single(self,name,prefix):
		""" update the label to the given label"""
		full_name= self.label
		short_name= full_name.replace(name,'')
		new_label= prefix+short_name
		self.label = new_label

	def reset_label(self):
		full_name= self.name
		self.label = full_name
