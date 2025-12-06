from pathlib import Path
from typing import Callable, Dict, List, Tuple
import timeit

try:
    from .boyer_moore import boyer_moore_search
    from .kmp import kmp_search
    from .rabin_karp import rabin_karp_search
except ImportError:
    import sys

    sys.path.append(str(Path(__file__).resolve().parent))
    from boyer_moore import boyer_moore_search
    from kmp import kmp_search
    from rabin_karp import rabin_karp_search

SearchFunc = Callable[[str, str], int]
DATA_DIR = (Path(__file__).resolve().parent / "data").resolve()
PATTERN_CHOICES = {
    "article1": ("жадібний алгоритм", "алгоритм Гровера для пошуку"),
    "article2": ("Рекомендаційні системи є важливою складовою", "нейронні мережі рекомендацій"),
}


def benchmark(func: SearchFunc, text: str, pattern: str, *, repeat: int = 5, number: int = 5) -> float:
    timer = timeit.Timer(lambda: func(text, pattern))
    runs = timer.repeat(repeat=repeat, number=number)
    return min(runs) / number


def select_existing_pattern(text: str, length: int = 32) -> str:
    cleaned = " ".join(text.split())
    if not cleaned:
        return ""
    snippet = cleaned[:length]
    next_char = cleaned[length:length + 1]
    if " " in snippet and next_char and not next_char.isspace():
        snippet = snippet.rsplit(" ", 1)[0]
    if snippet:
        return snippet
    return cleaned.split(" ", 1)[0]


def benchmark_on_text(name: str, text: str, *, existing: str, missing: str) -> List[Tuple[str, str, float]]:
    algorithms: Dict[str, SearchFunc] = {
        "Boyer-Moore": boyer_moore_search,
        "KMP": kmp_search,
        "Rabin-Karp": rabin_karp_search,
    }
    results: List[Tuple[str, str, float]] = []
    for label, pattern in ("existing", existing), ("missing", missing):
        for alg_name, func in algorithms.items():
            time_per_run = benchmark(func, text, pattern)
            results.append((label, alg_name, time_per_run))
    return results


def load_text(path: Path) -> str:
    return path.read_text(encoding="utf-8-sig")


def choose_patterns(name: str, text: str) -> Tuple[str, str]:
    custom = PATTERN_CHOICES.get(name)
    if custom:
        existing, missing = custom
        if existing in text:
            if missing in text:
                missing = f"{missing} (absent)"
            return existing, missing
    existing = select_existing_pattern(text)
    missing = f"{existing} (missing)" if existing else ""
    return existing, missing


def _print_results(name: str, results: List[Tuple[str, str, float]]) -> None:
    for label in ("existing", "missing"):
        filtered = [r for r in results if r[0] == label]
        if not filtered:
            continue
        fastest = min(filtered, key=lambda r: r[2])
        print(f"  [{label}] fastest: {fastest[1]} ({fastest[2]:.6f} s/run)")
        for _, alg_name, timing in filtered:
            print(f"    {alg_name:12} {timing:.6f} s/run")


def main() -> None:
    data_dir = DATA_DIR if DATA_DIR.exists() else (Path.cwd() / "data")
    article_paths = {
        "article1": data_dir / "article1.txt",
        "article2": data_dir / "article2.txt",
    }

    for name, path in article_paths.items():
        if not path.exists():
            print(f"[skip] {path} not found")
            continue

        text = load_text(path)
        existing_pattern, missing_pattern = choose_patterns(name, text)
        if not existing_pattern:
            print(f"[skip] {name}: file is empty")
            continue

        print(f"\n{name} ({path}):")
        print(f" existing pattern: {existing_pattern!r}")
        print(f" missing pattern: {missing_pattern!r}")

        results = benchmark_on_text(name, text, existing=existing_pattern, missing=missing_pattern)
        _print_results(name, results)


if __name__ == "__main__":
    main()
