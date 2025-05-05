"""
Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов в тексте, окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.

Пример использования:"""
import re


def highlight_keywords(text_, keywords_):
    for keyword in keywords_:
        text_ = re.sub(rf'\b{keyword}\b', lambda match: f'*{match.group()}*', text_, flags=re.IGNORECASE)
    return text_


text = "This is a sample text. We need to highlight Python and programming."

keywords = ["python", "programming"]

highlighted_text = highlight_keywords(text, keywords)

print(highlighted_text)

# Вывод: "This is a sample text. We need to highlight *Python* and *programming*."
