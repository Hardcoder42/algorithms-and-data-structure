1.
def has_duplicates(arr):
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                return True
    return False

#данный алгоритм представляет собой квадратичную сложность 0(n²) за счет двух циклов и сравнения. улучшить можно через использование множества set, которое содержит лишь уникальные значения, и цикл будет лишь один, имеющий линейную сложность.

2.
def find_max(arr):
    max_val = arr[0]
    for val in arr:
        if val > max_val:
            max_val = val
    return max_val

#данный алгоритм представляет собой линейную сложность 0(n), цикл один, 1 элемент взят за основу, сравнивается с остальными, вывод максимального значения по окончанию цикла

3.
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

#данный алгоритм представляет собой квадратичную сложность 0(n^2), за счет двух циклов и операции обмена по завершении

4.
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

#данный алгоритм представляет собой линейно логарифмическую сложность 0(n log n), в которой имеются 3 цикла (по факту 2) и их слияние в конце путем конкатенации. Но в худшем случае(когда опора pivot становится наименьшим/наибольшим элемкнтом в массиве), данный алгоритм уходит в еще большую глубину рекурсии и его сложность становится квадратичной 0(n²)

5.
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

#данный алгоритм представляет собой экспоненциальную сложность 0(φⁿ)), это один из самых неэффективных способов вычисления чисел Фибоначчи. Улучшить - итеративный алгоритм без сохранения последовательности сложности 0(n), память 0(1).