from typing import Any, List, Tuple


_MISSING = object()


class HashTable:
    def __init__(self, size: int = 10) -> None:
        if size <= 0:
            raise ValueError("Size must be positive")
        self.size = size
        self.table: List[List[Tuple[Any, Any]]] = [[] for _ in range(self.size)]

    def hash_function(self, key: Any) -> int:
        return hash(key) % self.size

    def insert(self, key: Any, value: Any) -> bool:
        key_hash = self.hash_function(key)
        bucket = self.table[key_hash]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)
                return True
        bucket.append((key, value))
        return True

    def get(self, key: Any, default: Any = None) -> Any:
        key_hash = self.hash_function(key)
        bucket = self.table[key_hash]
        for k, v in bucket:
            if k == key:
                return v
        return default

    def delete(self, key: Any) -> Any:
        key_hash = self.hash_function(key)
        bucket = self.table[key_hash]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                bucket.pop(i)
                return v
        raise KeyError(f"Key not found: {key!r}")

    def __contains__(self, key: Any) -> bool:
        return self.get(key, default=_MISSING) is not _MISSING

    def __len__(self) -> int:
        return sum(len(bucket) for bucket in self.table)

    def __repr__(self) -> str:
        items = []
        for bucket in self.table:
            items.extend(f"{k!r}: {v!r}" for k, v in bucket)
        return "{" + ", ".join(items) + "}"


def _demo() -> None:
    H = HashTable(5)
    H.insert("apple", 10)
    H.insert("orange", 20)
    H.insert("banana", 30)
    print("Initial table:", H)
    removed = H.delete("orange")
    print("deleted:", removed)
    print("after delete:", H)


if __name__ == "__main__":
    _demo()
