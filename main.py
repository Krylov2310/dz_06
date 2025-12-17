from random import randint
import os
import platform
import time

list_size = [10, 100, 1000]


def info():
    print('\033[33mДомашнее задание 6\n'
          '"Быстрая сортировка"\n'
          'Студент Крылов Эдуард Васильевич\n'
          'Дата: 17.12.2025г.\033[0m')


# Очистка консоли
def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')  # From Linux


# Переход по заданиям
def any_key():
    input('\n\033[33mНажмите "Enter" для продолжения...\033[0m')


# Отсчёт начала времени
def start_time():
    start_time_ = time.perf_counter()  # точное время в секундах
    return start_time_


# Отсчёт конца времени
def print_time(get_time):
    end_time_ = time.perf_counter()
    elapsed_time = end_time_ - get_time
    print(f'\033[31mВремя: {elapsed_time:.6f}\033[0m')


# Генератор списка
def list_generate(size_list):
    arr1 = []
    for i in range(size_list):
        arr1.append(randint(1, 1000))
    return arr1


# 01
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        # print(f'Проверка элементов в очереди: "{self.items}"')
        return len(self.items) == 0

    def enqueue(self, items):
        self.items.append(items)
        # print(f'Добавлен элемент: "{items}"')

    def dequeue(self):
        if not self.is_empty():
            # print(f'Удален первый элемент: "{self.items[0]}"')
            return self.items.pop(0)

    def peek(self):
        if not self.is_empty():
            # print(f'Первый элемент списка: "{self.items[0]}"')
            return self.items[0]

    def size(self):
        return len(self.items)

    def __str__(self):
        # Строковое представление очереди (для отладки).
        return "Queue: " + " <- ".join(map(str, self.items))


def print_queue():
    print('\n\033[34m01 Процесс: Основные операции очереди.\033[0m')
    t = start_time()
    queue = Queue()
    list_queue = [10, 'Synergy', 12.6, 'tester']
    for i in list_queue:
        print(f'Добавлен элемент: {i}')
        queue.enqueue(i)  # Добавление в список
    print_time(t)
    t = start_time()
    print(f'Пустой список: {queue.is_empty()}')  # Проверка пустого списка
    print(f'Сформированные задачи: {queue}')
    print_time(t)
    t = start_time()
    print(f'Первый элемент: {queue.peek()}')  # Просмотр первого элемента
    print_time(t)
    t = start_time()
    print(f'Размер списка: {queue.size()}')  # Размер списка
    print_time(t)
    t = start_time()
    print(f'Удаление первого элемента: {queue.dequeue()}')  # Удаление первого элемента
    print(f'Сформированные задачи: {queue}')
    print_time(t)
    t = start_time()
    print(f'Первый элемент: {queue.peek()}')  # Просмотр первого элемента
    print_time(t)
    t = start_time()
    print(f'Размер списка: {queue.size()}')  # Размер списка
    print_time(t)


# 02
def process_tasks(task_list):
    # Создаём очередь
    task_queue = Queue()
    # Добавляем все задачи в очередь
    for task in task_list:
        task_queue.enqueue(task)

    print('Очередь задач сформирована:')
    print(task_queue)
    print('-' * 40)

    current_time = 0  # Текущее время (в условных единицах)

    while not task_queue.is_empty():
        # Берём первую задачу из очереди
        task_name, task_duration = task_queue.dequeue()

        # Время начала выполнения
        start_timer = current_time

        end_timer = current_time + task_duration

        print(f'Задача: {task_name}')
        print(f'  Начало: {start_timer} минут.')
        print(f'  Длительность: {task_duration} минут.')
        print(f'  Завершение: {end_timer} минут.')
        # Обновляем текущее время
        current_time = end_timer
        print('-' * 30)
        print('\033[34mВсе задачи выполнены!\033[0m')


def print_task():
    print('\n\033[34m02 Процесс: Основные операции очереди.\033[0m')
    # Список задач: (название, время выполнения)
    tasks = [
        ('Сделать домашнюю работу', 120),
        ('Проверить почту', 10),
        ('Обеденный перерыв', 60),
        ('Подготовить презентацию', 75),
        ('Настроить 1С в бухгалтерии', 45)
    ]
    # Запускаем моделирование
    process_tasks(tasks)


# 03
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                # print(f'1: {left_half[i]} < {right_half[j]}')
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            # print(f'2: {i} < {len(left_half)}')
            arr[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
    return arr


# 04
def buble_sort(arr_1):
    n = len(arr_1)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr_1[j] > arr_1[j + 1]:
                arr_1[j], arr_1[j + 1] = arr_1[j + 1], arr_1[j]
                swapped = True
        if not swapped:
            break
    return arr_1


def print_merge():
    print('\033[33m\n003 Функция для реализации сортировки слиянием (MergeSort).\033[0m')
    for i in list_size:
        arr = list_generate(i)
        arr_1 = arr.copy()

        print(f'\033[35mИсходный список: {len(arr)} элементов:\033[0m\n{arr}')
        t = start_time()

        print(f'\033[32mОтсортированный список (MergeSort):\033[0m\n{merge_sort(arr)}')
        # print(f'Прошло операций (MergeSort): {count}')
        print_time(t)
        t = start_time()
        print(f'\033[34mОтсортированный список (BubleSort):\033[0m\n{buble_sort(arr_1)}')
        print_time(t)


# Пример использования
if __name__ in '__main__':
    clear_screen()
    info()
    print_queue()  # 01
    any_key()
    print_task()  # 02
    any_key()
    print_merge()

print('\n\033[33mДомашнее задание закончено.\033[0m')
