"""03 ================================================
Написать функцию get_cars_by_color(), которая принимает
список объектов класса Car и цвет и возвращает iterator объект машин этого цвета.

Напечатать этот список, выводя название модели, год и цвет.
Использовать filter и lambda функции.
"""
from typing import Iterator, List

from prasctice_14_1 import Car
from prasctice_14_2 import cars


def get_cars_by_color(vehicles: List[Car], color: str) -> Iterator[Car]:
    pass


# Car(brand=Golf, year=2020, color=Red)
# Car(brand=Golf, year=2020, color=Red)
# Car(brand=Skoda, year=2022, color=Red)
# Car(brand=Sharan, year=2016, color=Red)
# Car(brand=Nissan, year=2013, color=Red)
