def rabin_karp_search(text: str, pattern: str, base: int = 256, prime: int = 101) -> int:
    if pattern == "":
        return 0
    m, n = len(pattern), len(text)
    if m > n:
        return -1

    def polynomial_hash(s: str) -> int:
        length = len(s)
        value = 0
        for idx, ch in enumerate(s):
            power = pow(base, length - idx - 1, prime)
            value = (value + ord(ch) * power) % prime
        return value

    pattern_hash = polynomial_hash(pattern)
    window_hash = polynomial_hash(text[:m])
    h_multiplier = pow(base, m - 1, prime)

    for i in range(n - m + 1):
        if pattern_hash == window_hash:
            if text[i : i + m] == pattern:
                return i
        if i < n - m:
            window_hash = (window_hash - ord(text[i]) * h_multiplier) % prime
            window_hash = (window_hash * base + ord(text[i + m])) % prime
            if window_hash < 0:
                window_hash += prime
    return -1
