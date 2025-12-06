# GOIT Algorithms Homework 05 / ДЗ 05 Алгоритми

[English](#english) | [Українська](#українська)

---

## English
### Overview
Three independent tasks on search algorithms:
- Hash table with insert/get/delete.
- Binary search that returns iteration count and upper bound.
- Substring search (Boyer–Moore, KMP, Rabin–Karp) with benchmarks on two articles.

### Project layout
- `task_1/task_1.py` — hash table implementation (chaining).
- `task_1/test_task_1.py` — tests for task 1.
- `task_2/task_2.py` — binary search with iterations and upper bound.
- `task_2/test_task_2.py` — tests for task 2.
- `task_3/boyer_moore.py`, `task_3/kmp.py`, `task_3/rabin_karp.py` — algorithms.
- `task_3/task_3.py` — benchmark runner.
- `task_3/test_task_3.py` — tests for task 3.
- `task_3/results.md` — benchmark results (EN/UA).
- `task_3/data/article1.txt`, `task_3/data/article2.txt` — texts for benchmarks.

### How to run
- Task 1 demo: `python task_1/task_1.py`
- Task 2 demo: `python task_2/task_2.py` (prints steps and upper bounds for sample targets)
- Task 3 benchmarks: `python task_3/task_3.py` (skips if article file is missing)
- All tests: `python -m pytest`
- Per-task tests: `python -m pytest task_1/test_task_1.py` (and similarly for task_2, task_3)

### Notes
- HashTable: `insert`, `get`, `delete` (raises `KeyError` if key absent).
- Binary search: returns `(iterations, upper_bound)` where upper_bound is the smallest value `>= target` or `None`.
- String search: each algorithm returns start index or `-1`; benchmarks choose one existing and one fabricated (absent) pattern per article. Results summarized in `task_3/results.md`.

---

## Українська
### Огляд
Три незалежні задачі з алгоритмів пошуку:
- Хеш-таблиця з операціями вставки/отримання/видалення.
- Двійковий пошук, що повертає кількість ітерацій та верхню межу.
- Пошук підрядка (Боєр–Мур, Кнут–Морріс–Пратт, Рабін–Карп) з бенчмарками на двох статтях.

### Структура
- `task_1/task_1.py` — реалізація хеш-таблиці (ланцюги).
- `task_1/test_task_1.py` — тести для завдання 1.
- `task_2/task_2.py` — двійковий пошук з підрахунком ітерацій і верхньою межею.
- `task_2/test_task_2.py` — тести для завдання 2.
- `task_3/boyer_moore.py`, `task_3/kmp.py`, `task_3/rabin_karp.py` — алгоритми.
- `task_3/task_3.py` — запуск бенчмарків.
- `task_3/test_task_3.py` — тести для завдання 3.
- `task_3/results.md` — результати бенчмарків (дві мови).
- `task_3/data/article1.txt`, `task_3/data/article2.txt` — тексти для вимірів.

### Як запустити
- Демонстрація 1: `python task_1/task_1.py`
- Демонстрація 2: `python task_2/task_2.py` (виводить кроки пошуку та верхні межі для прикладів)
- Бенчмарки 3: `python task_3/task_3.py` (пропускає файл, якщо його немає)
- Всі тести: `python -m pytest`
- Тести окремо: `python -m pytest task_1/test_task_1.py` (та інші за аналогією)

### Примітки
- HashTable: `insert`, `get`, `delete` (підіймає `KeyError`, якщо ключ відсутній).
- Двійковий пошук: повертає `(iterations, upper_bound)`, де upper_bound — найменше `>= target` або `None`.
- Пошук підрядка: кожен алгоритм повертає індекс або `-1`; бенчмарки беруть один наявний і один вигаданий патерн на статтю. Підсумки в `task_3/results.md`.
