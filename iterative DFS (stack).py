class Node:
	def __init__(self, value):
		self.value = value
		
		self.outbound = []
		self. inbound = []
	
	def point_to(self, other):
		self.outbound.append(other)
		other.inbound.append(self)
	
	def __str__(self):
		return f"Node({self.value})"

#обход в глубину с возвратом списка узлов со стеком
class Graph:
	def __init__(self, root):
		self._root = root#стартовая точка
	
	def dfs(self):
		visited = set()#посещенные узлы, множество быстрее списка
		result = []#список результатов
		stack = []#стек для узлов
	
		stack.append(self._root)#корневой узел
		while stack:
			vertex = stack.pop()#вершина из стека
			
			if vertex is not visited:
				visited.add(vertex)
				result.append(vertex)
				
				for neighbor in reversed(vertex.outbound):
					if neighbor not in visited:
						stack.append(neighbor)
		
		return result	
	

#создание графа
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

g = Graph(a)#начинаем с узла "а"
result = g.dfs()#запуск обхода

#резултс
for node in result:
	print(node)