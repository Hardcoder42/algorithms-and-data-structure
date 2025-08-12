class Stack:
    def __init__(self):
        self.items = []
        # список

    def is_empty(self):
        return len(self.items) == 0
        # пуст ли стек

    def push(self, item):
        self.items.append(item)
        # добавление элемента в конец списка

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
        # удаляет и возвращает элемент из вершины стека + проверка не пуст ли

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
        # возвращает элемент из вершины без удаления + проверка

    def size(self):
        return len(self.items)
        # возвращает количество элементов

def tokenize(expr):
    return expr.strip().split()
    # разбиваем строку по пробелам

def rpn(expr):
    stack = Stack()
    tokens = tokenize(expr)

    for token in tokens:
        if token.replace('.', '', 1).isdigit():
            stack.push(float(token))
        elif token in ['+', '-', '/', '*']:
            if stack.size() < 2:
                raise ValueError("Недостаточно операндов в стеке")
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                result = a + b
            elif token == '-':
                result = a - b
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("Деление на ноль")
                result = a / b
            elif token == '*':
                result = a * b
            stack.push(result)
        else:
            raise ValueError(f"Неизвестный токен: {token}")

    if stack.size() != 1:
        raise ValueError("Ошибка: в стеке больше одного значения в конце")
    return stack.pop()

expr = "3 4 + 2 * 7 /"
print(rpn(expr))