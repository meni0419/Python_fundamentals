"""Напишите функцию sort_dicts_by_key(), которая принимает:
    - список словарей и
    - ключ, по которому нужно отсортировать список словарей.
Функция должна быть аннотирована с помощью аннотаций типов.
"""
from pprint import pprint
from typing import Any


def sort_dicts_by_key(dicts: list[dict[str, Any]], key: str) -> list[dict[str, Any]]:
    return sorted(dicts, key=lambda d: d.get(key, None))


example_dicts = [
    {"name": "Alice", "age": 25},
    {"name": "Bob", "age": 20},
    {"name": "Charlie", "age": 30}
]

print("=========sort by key 'name'=========")
pprint(sort_dicts_by_key(example_dicts, "name"))

print("=========sort by key 'age'=========")
pprint(sort_dicts_by_key(example_dicts, "age"))
