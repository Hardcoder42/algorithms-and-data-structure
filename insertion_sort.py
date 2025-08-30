def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):#0 считается sorted
    	current = arr[i]#значение текущего elem
    	j = i - 1#значение крайнего sorted
    	while j >= 0 and arr[j] > current:#пока не вышли за границы влево и sorted не стал меньше/равен current
    		arr[j + 1] = arr[j]#важно, пока условие выполняется, сдвигаем sorted вправо 
    		j -= 1#сдвигаемся по sorted на шаг влево 
    	arr[j + 1] = current#j теперь на позиции, где while не выполняется, соответственно, вставляем current справа


# Пример использования:
my_list = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_list)
print("Отсортированный список:", my_list)