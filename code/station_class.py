class Station():
	"""docstring for ClassName"""

	def __init__(self,name,label,importance,location,neighbours):
		self.name = name
		self.label = label
		self.importance = importance
		self.location = location
		self.neighbours = neighbours

	def information(self):
		return '{} {} {} {}'.format(self.name, self.label, self.importance, self.location, self.neighbours)







		#[(obj.name,n[0],n[1]) for obj in gc.get_objects() if isinstance(obj, st.Station) for n in obj.neighbours]
