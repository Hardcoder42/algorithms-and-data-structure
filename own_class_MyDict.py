class MyDict:
	def __init__(self):
		"""создаем словарь"""
		self._d = {}
	
	def __getitem__(self, k):
		"""получаем значение через dict[key]"""
		if k not in self._d:
			return None #согласно задания
		return self._d[k]
		
	
	def __setitem__(self, k, v):
		"""устанавливаем значение через dict[key] = value"""
		self._d[k] = v
	
	def __delitem__(self, k):
		"""удаляем значение через del dict[key]"""
		del self._d[k]
	
	def keys(self):
		"""выводим список ключей"""
		return list(self._d.keys())
	
	def values(self):
		"""выводим список значений"""
		return list(self._d.values())
	
	def items(self):
		"""выводим список пар ключ-значение"""
		return list(self._d.items())
	
	def __str__(self):
		"""строковое представление словаря"""
		return str(self._d)
		
	def __contains__(self, k):
		"""проверяем наличие ключа, опциональный метод, но необходим для проверки наличия ключа в словаре"""
		return k in self._d

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
		


"""
#Hardcoder mode
class MyDict:
	def __init__(self): self._d = {}
	def __getitem__(self, k): return self._d.get(k)
	def __setitem__(self, k, v): self._d[k] = v
	def __delitem__(self, k): del self._d[k]
	def keys(self): return list(self._d.keys())
	def values(self): return list(self._d.values())
	def items(self): return list(self._d.items())
	def __str__(self): return str(self._d)
	def __contains__(self, k): return k in self._d
"""