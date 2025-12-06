from task_3.task_3 import (
    boyer_moore_search,
    kmp_search,
    rabin_karp_search,
    benchmark,
)


TEXT = "abracadabra and other magic words"


def _common_tests(search_func):
    assert search_func(TEXT, "abra") == 0
    assert search_func(TEXT, "magic") == 22
    assert search_func(TEXT, "missing") == -1
    assert search_func(TEXT, "") == 0


def test_boyer_moore():
    _common_tests(boyer_moore_search)


def test_kmp():
    _common_tests(kmp_search)


def test_rabin_karp():
    _common_tests(rabin_karp_search)


def test_benchmark_returns_float():
    t = benchmark(kmp_search, TEXT, "abra", repeat=2, number=2)
    assert isinstance(t, float)
    assert t >= 0.0
