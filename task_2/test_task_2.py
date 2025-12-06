from task_2.task_2 import binary_search


def test_exact_hit():
    iterations, upper = binary_search([1.0, 2.0, 3.0], 2.0)
    assert upper == 2.0
    assert iterations >= 1


def test_between_values():
    iterations, upper = binary_search([1.0, 3.0, 5.0], 4.0)
    assert upper == 5.0
    assert iterations >= 1


def test_below_minimum():
    iterations, upper = binary_search([2.0, 4.0, 6.0], 1.0)
    assert upper == 2.0
    assert iterations >= 1


def test_above_maximum():
    iterations, upper = binary_search([2.0, 4.0, 6.0], 10.0)
    assert upper is None
    assert iterations >= 1


def test_duplicates_choose_first_upper_bound():
    iterations, upper = binary_search([1.0, 2.0, 2.0, 4.0], 2.0)
    assert upper == 2.0
    assert iterations >= 1


def test_empty_list():
    iterations, upper = binary_search([], 5.0)
    assert iterations == 0
    assert upper is None
