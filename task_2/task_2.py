from typing import List, Optional, Tuple


def binary_search(sorted_values: List[float], target: float) -> Tuple[int, Optional[float]]:
    low, high = 0, len(sorted_values) - 1
    iterations = 0
    upper_bound: Optional[float] = None

    while low <= high:
        iterations += 1
        mid = (high + low) // 2
        mid_value = sorted_values[mid]

        if mid_value >= target and (upper_bound is None or mid_value < upper_bound):
            upper_bound = mid_value

        if mid_value < target:
            low = mid + 1
        elif mid_value > target:
            high = mid - 1
        else:
            return iterations, mid_value

    if upper_bound is None and low < len(sorted_values):
        upper_bound = sorted_values[low]

    return iterations, upper_bound


def _demo() -> None:
    data = [-5.5, -1.0, 0.0, 2.2, 3.3, 4.4, 7.7]
    for value in (-10.0, -1.0, 1.5, 4.4, 6.0, 8.0):
        iters, upper = binary_search(data, value)
        upper_str = upper if upper is not None else "none (greater value not found)"
        print(f"find {value:>5}: {iters} steps, upper bound (smallest >= target) = {upper_str}")


if __name__ == "__main__":
    _demo()
