# lab_1

import random  # Імпортуємо модуль для генерації випадкових чисел
import time

def generate_random_array(n, lower_bound=0, upper_bound=100):
    """
    Генерує випадковий масив із n елементів у діапазоні від lower_bound до upper_bound.

    :param n: кількість елементів у масиві
    :param lower_bound: нижня межа для генерації чисел (включно)
    :param upper_bound: верхня межа для генерації чисел (включно)
    :return: список із випадковими числами
    """
    return [random.randint(lower_bound, upper_bound) for _ in range(n)]


# Виклик функції для створення масиву з 20 випадкових чисел
random_array = generate_random_array(5000, 0, 10000)
main_array = random_array[:]
print(F"random arr = {random_array}\n"
      F"main arr = {main_array}")  # Виведення згенерованого масиву


# BubbleSort
def BubbleSort(main_array):
    n = len(main_array)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if main_array[j] > main_array[j + 1]:
                main_array[j], main_array[j + 1] = main_array[j + 1], main_array[j]

    print("Sorted array:", main_array)


# InsertionSort
def InsertionSort(main_array):
    n = len(main_array)
    for i in range(1, n):
        insert_index = i
        current_value = main_array.pop(i)
        for j in range(i - 1, -1, -1):
            if main_array[j] > current_value:
                insert_index = j
        main_array.insert(insert_index, current_value)

    print("Sorted array with InsertionSort:", main_array)


# QuickSort
def quicksort(main_array):
    # Якщо масив містить один або менше елементів, він вже відсортований
    if len(main_array) <= 1:
        return main_array

    # Вибираємо опорний елемент (pivot) - середній елемент масиву
    pivot = main_array[len(main_array) // 2]

    # Створюємо три списки:
    # 1. Елементи, що менші за опорний
    left = [x for x in main_array if x < pivot]

    # 2. Елементи, що дорівнюють опорному
    middle = [x for x in main_array if x == pivot]

    # 3. Елементи, що більші за опорний
    right = [x for x in main_array if x > pivot]

    # Рекурсивно сортуємо ліву та праву частини і об'єднуємо всі три частини
    return quicksort(left) + middle + quicksort(right)


quicksort(main_array)
print(main_array)


# Hoare's QuickSort
def quicksort(main_array, low, high):
    if low < high:
        # Отримати індекс поділу
        pi = partition(main_array, low, high)

        # Рекурсивно сортувати елементи перед і після поділу
        quicksort(main_array, low, pi)
        quicksort(main_array, pi + 1, high)

def partition(main_array, low, high):
    # Вибрати середній елемент як опорний
    pivot = main_array[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        # Шукати елемент більший за опорний
        i += 1
        while main_array[i] < pivot:
            i += 1

        # Шукати елемент менший за опорний
        j -= 1
        while main_array[j] > pivot:
            j -= 1

        # Якщо індекси перетнулися, повернути індекс поділу
        if i >= j:
            return j

        # Якщо ні, поміняти місцями
        main_array[i], main_array[j] = main_array[j], main_array[i]


# Приклад використання:
quicksort(main_array, 0, len(main_array) - 1)
print("Відсортований масив:", main_array)


