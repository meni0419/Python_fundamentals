"""09 ==========================================
Напишите функцию, которая получает на вход
    две строки с перечислением интересов и хобби двух пользователей, и
    вычисляет процент совпадения.

Процент рассчитывается, как отношение числа совпадений к максимальному числу интересов
ОДНОГО ИЗ участников.
(например: у 1-го - 3 хобби, у 2-го - 4 хобби
=> max будет равен 4)

Использовать множества.
"""


def match_percentage(interests_1: str, interests_2: str) -> float:
    interests_1_set = set(interests_1.split())
    interests_2_set = set(interests_2.split())
    intersection = interests_1_set.intersection(interests_2_set)
    res = len(intersection) / (len(interests_1_set) + len(interests_2_set)) * 100
    return res


user1_interests = "путешествия, фотография, кино, музыка"
user2_interests = "фотография, кино, литература, спорт"

result = match_percentage(user1_interests, user2_interests)
print(f"Процент совпадения интересов: {result:.2f} %")
# Процент совпадения интересов: 25.00 %
