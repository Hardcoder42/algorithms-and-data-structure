from collections import deque

class EmptyQueueError(Exception):
	"""Ошибка для пустой очереди"""
	pass

class Queue:
	def __init__(self):
		self._items = deque()
		#вместо долгого метода pop, используем коллекцию deque

	def enqueue(self, item):
		self._items.append(item)
		#добавляем в конец очереди
	
	def dequeue(self):
		if self.is_empty():
			raise EmptyQueueError("Очередь пуста: нельзя удалить ничто")
		return self._items.popleft()
		#вброс ошибки на случай пустоты/буст скорости за счет удаления последнего айтема без счета

	def is_empty(self):
		return len(self._items) == 0
		#проверка на наличие айтемов в очереди
	
	def size(self):
		return len(self._items)
		#количество айтемов
	
	def __str__(self):
		return f"Очередь: ({list(self._items)})"
		#красивый вывод списка

#реализация кода
q = Queue()
q.enqueue(11)
q.enqueue(22)
q.enqueue(33)

print(q.is_empty())#пусто ли
print(q)#список полностью
print(q.dequeue())#удаляем
print(q.size())#сколько осталось
print(q.dequeue())#удаляем
print(q.size())#сколько осталось
print(q.dequeue())#удаляем
print(q.is_empty())#пусто ли теперь?