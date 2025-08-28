from collections import deque

class Node:
	def __init__(self, value):
		self.value = value
		self.outbound = []
		self.inbound = []
	
	def point_to(self, other):
		self.outbound.append(other)
		other.inbound.append(self)
	
	def __str__(self):
		return f'Node({self.value})'

class Graph:
	def __init__(self, root):
		self._root = root

	def bfs(self):
		visited = set()#множество посещенных
		result = []#список обхода
		queue = deque()#двусторонняя очередь

    #начинаем с корневой вершины    
		queue.append(self._root)
		visited.add(self._root)

		while queue:
			current_node = queue.popleft()
			result.append(current_node)#посещаем вершину

			for neighbor in current_node.outbound:
				if neighbor not in visited:
					queue.append(neighbor)
					visited.add(neighbor)
					
		return result

#реализация кода
a = Node('a')
b = Node('b')
c = Node('c')
d = Node('d')
e = Node('e')
f = Node('f')
g = Node('g')
h = Node('h')
i = Node('i')
k = Node('k')
a.point_to(b)
b.point_to(c)
c.point_to(d)
d.point_to(a)
b.point_to(d)
a.point_to(e)
e.point_to(f)
e.point_to(g)
f.point_to(i)
f.point_to(h)
g.point_to(k)

g = Graph(a)#граф с начальной вершиной
result = g.bfs()#запуск обхода

for node in result:
	print(node)