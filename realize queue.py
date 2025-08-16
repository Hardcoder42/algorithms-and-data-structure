from collections import deque

class EmptyQueueError(Exception):
    pass
    # custom error

class TaskQueue:
    def __init__(self):
        self._items = deque()

    def add_task(self, item):
        self._items.append(item)
        # добавляем задачу в очередь

    def get_next_task(self):
        if self.is_empty():
            raise EmptyQueueError("Очередь пуста: невозможно извлечь ничто")  # вместо None
        return self._items.popleft()
        # извлекаем следующую задачу

    def is_empty(self):
        return len(self._items) == 0
        # проверка на пустоту

    def size(self):
        return len(self._items)
        # остаток задач в очереди


class Task:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name
        # строковое представление


# реализация кода
if __name__ == "__main__":
    q = TaskQueue()#создаем очередь
    tasks = [Task(f"Задача {i}") for i in range(1, 4)]#создаем задачи
    for task in tasks:
        q.add_task(task)#создаем очередь задач

    try:
        while not q.is_empty():#пока очередь не пуста
            next_task = q.get_next_task()#берем задачу из начала
            print(f"Следующая задача: {next_task.name}")
            print(f"Задач осталось: {q.size()}")
            print("-" * 30)
        print(f"Очередь пуста: {q.is_empty()}")
    except EmptyQueueError as e:
        print(f"Ошибка: {e}")