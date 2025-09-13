class MyDict:
	def __init__(self):
		"""структура в виде списков ключ-значение"""
		self._keys = []#под ключи
		self._values = []#под значения
	
	def __getitem__(self, k):
		"""получаем значение по ключу"""
		if k in self._keys:
			index = self._keys.index(k)
			return self._values[index]
		return None #согласно задания
			
	def __setitem__(self, k, v):
		"""добавление/обновление пары ключ-значение"""
		if k in self._keys:
			index = self._keys.index(k)
			self._values[index] = v
		else:
			self._keys.append(k)
			self._values.append(v)
	
	def __delitem__(self, k):
		"""удаляем значение по ключу"""
		if k in self._keys:
			index = self._keys.index(k)
			del self._keys[index]
			del self._values[index]
		else:
			raise KeyError(f"Key '{k}' not found")
			
	def keys(self):
		"""выводим список ключей"""
		return self._keys.copy()
	
	def values(self):
		"""выводим список значений"""
		return self._values.copy()
	
	def items(self):
		"""выводим список пар ключ-значение"""
		return [(self._keys[i], self._values[i]) for i in range(len(self._keys))]
	def __str__(self):
		"""строковое представление словаря"""
		items = []
		for i in range(len(self._keys)):
			items.append(f"{self._keys[i]}: {self._values[i]}")
		return "{" + ", ".join(items) + "}"
		
	def __contains__(self, k):
		"""проверяем наличие ключа, опциональный метод, но необходим для проверки наличия ключа среди имеющихся"""
		return k in self._keys

my_dict = MyDict()
my_dict['name'] = 'Alice'
my_dict['age'] = 30

print(my_dict['name'])
print(my_dict['age'])
print(my_dict['city'])
print('city' in my_dict)

del my_dict['age']
print(my_dict.keys())
print(my_dict.values())
print(my_dict)
