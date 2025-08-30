def selection_sort(arr):
    n = len(arr)#сохраняем длину массива
    for i in range(n):#поиск по всем элементам
    	min_index = i#первый элемент за min
    	for j in range(i + 1, n):#поиск по unsorted
    		if arr[j] < arr[min_index]:#если меньше
    			min_index = j#обновляем индекс min
    	arr[i], arr[min_index] = arr[min_index], arr[i]#заменяем min с i местами

# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
selection_sort(my_list)
print("Отсортированный список:", my_list)