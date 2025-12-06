# Substring Search Benchmarks / Результати пошуку підрядків

[English](#english) | [Українська](#українська)

---

## English
Measurements from `python task_3/task_3.py` (time per run in seconds).

### article1 (`task_3/data/article1.txt`)
| Pattern                                  | Boyer-Moore | KMP       | Rabin-Karp | Fastest |
|------------------------------------------|-------------|-----------|------------|---------|
| `жадібний алгоритм`                      | 0.000008    | 0.000025  | 0.000057   | Boyer-Moore |
| `алгоритм Гровера для пошуку` (missing)  | 0.000111    | 0.000798  | 0.001650   | Boyer-Moore |

### article2 (`task_3/data/article2.txt`)
| Pattern                                              | Boyer-Moore | KMP       | Rabin-Karp | Fastest |
|------------------------------------------------------|-------------|-----------|------------|---------|
| `Рекомендаційні системи є важливою складовою`        | 0.000021    | 0.000159  | 0.000352   | Boyer-Moore |
| `нейронні мережі рекомендацій` (missing)             | 0.000164    | 0.001152  | 0.002396   | Boyer-Moore |

### Overall
- Boyer–Moore was the fastest in all measured cases.
- Patterns were chosen from meaningful phrases in each article; missing patterns are realistic but absent.

---

## Українська
Вимірювання з `python task_3/task_3.py` (час на один запуск у секундах).

### article1 (`task_3/data/article1.txt`)
| Патерн                                    | Boyer-Moore | KMP       | Rabin-Karp | Найшвидший |
|-------------------------------------------|-------------|-----------|------------|------------|
| `жадібний алгоритм`                       | 0.000008    | 0.000025  | 0.000057   | Boyer-Moore |
| `алгоритм Гровера для пошуку` (вигаданий) | 0.000111    | 0.000798  | 0.001650   | Boyer-Moore |

### article2 (`task_3/data/article2.txt`)
| Патерн                                               | Boyer-Moore | KMP       | Rabin-Karp | Найшвидший |
|------------------------------------------------------|-------------|-----------|------------|------------|
| `Рекомендаційні системи є важливою складовою`        | 0.000021    | 0.000159  | 0.000352   | Boyer-Moore |
| `нейронні мережі рекомендацій` (вигаданий)           | 0.000164    | 0.001152  | 0.002396   | Boyer-Moore |

### Підсумок
- Boyer–Moore був найшвидшим у всіх виміряних випадках.
- Патерни взяті з осмислених фраз у статтях; вигадані патерни правдоподібні, але відсутні в текстах.
