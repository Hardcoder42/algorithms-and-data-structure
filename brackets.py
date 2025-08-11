class Stack:
	def __init__(self):
		self.items = []
		#список
	
	def is_empty(self):
		return len(self.items) == 0
		#пуст ли стек
	
	def push(self, item):
		self.items.append(item)
		#добавление элемента в конец списка
	
	def pop(self):
		if not self.is_empty():
			return self.items.pop()
		else:
			raise IndexError("Stack is empty")
			#удаляет и возвращает элемент из вершины стека +проверка не пуст ли
	
	def peek(self):
		if not self.is_empty():
			return self.items[-1]
		else:
			raise IndexError("Stack is empty")
			#возвращает элемент из вершины без удаления + проверка
	
	def size(self):
		return len(self.items)
		#возвращает количество элементов
	
def is_balanced(expression):
		if not expression:
			return True
			#проверка на пустую строку
		stack = Stack()
		opening = {"(", "[", "{", "<"}
		closing = {")": "(", "]": "[", "}": "{", ">": "<"}
		
		for char in expression:
			if char in opening:#открывающая
				stack.push(char)
			elif char in closing:#закрывающая
				if stack.is_empty():
					return False
				last_opening = stack.pop()
				if closing[char] != last_opening:
					return False
		return stack.is_empty()
		
#реализация стека
print(is_balanced("([]{}<>)"))
print(is_balanced("([)]"))
print(is_balanced("{[}"))
print(is_balanced("()"))