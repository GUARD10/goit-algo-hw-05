import pytest

from task_1.task_1 import HashTable


def test_set_and_get():
    table = HashTable(size=3)
    table.insert("a", 1)
    table.insert("b", 2)
    assert table.get("a") == 1
    assert table.get("b") == 2
    assert table.get("missing", default=None) is None


def test_update_overwrites_value():
    table = HashTable(size=2)
    table.insert("key", 1)
    table.insert("key", 5)
    assert table.get("key") == 5
    assert len(table) == 1


def test_delete_returns_value_and_removes():
    table = HashTable(size=2)
    table.insert("x", 10)
    table.insert("y", 20)
    removed = table.delete("x")
    assert removed == 10
    assert "x" not in table
    assert len(table) == 1


def test_delete_missing_raises_keyerror():
    table = HashTable(size=2)
    table.insert("x", 10)
    with pytest.raises(KeyError):
        table.delete("absent")


def test_delete_with_collisions():
    table = HashTable(size=1)  # force collisions
    table.insert("k1", 1)
    table.insert("k2", 2)
    removed = table.delete("k1")
    assert removed == 1
    assert table.get("k1") is None
    assert table.get("k2") == 2
    assert len(table) == 1
