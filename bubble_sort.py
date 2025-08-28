def bubble_sort(arr):
	n = len(arr)#длинна
	for i in range(n - 1):#внешний цикл
		for j in range(n - i - 1):#внутр цикл
			if arr[j] > arr[j + 1]:#сравнение
				arr[j], arr[j + 1] = arr[j + 1], arr[j]#меняем
	return arr
my_list = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_list)
print("Отсортированный список:", my_list)