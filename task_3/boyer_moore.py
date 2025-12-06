from typing import Dict


def build_shift_table(pattern: str) -> Dict[str, int]:
    table: Dict[str, int] = {}
    length = len(pattern)
    for idx, ch in enumerate(pattern[:-1]):
        table[ch] = length - idx - 1
    table.setdefault(pattern[-1], length)
    return table


def boyer_moore_search(text: str, pattern: str) -> int:
    if pattern == "":
        return 0
    m, n = len(pattern), len(text)
    if m > n:
        return -1
    shift_table = build_shift_table(pattern)
    i = 0
    while i <= n - m:
        j = m - 1
        while j >= 0 and text[i + j] == pattern[j]:
            j -= 1
        if j < 0:
            return i
        i += shift_table.get(text[i + m - 1], m)
    return -1
