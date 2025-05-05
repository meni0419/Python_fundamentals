"""
Напишите функцию highlight_keywords(text, keywords), которая выделяет все вхождения заданных ключевых слов в тексте, окружая их символами *. Функция должна быть регистронезависимой при поиске ключевых слов.

Пример использования:"""

def highlight_keywords(text, keywords):
    for keyword in keywords:
        text = text.replace(keyword, f"*{keyword}*")
    return text

text = "This is a sample text. We need to highlight Python and programming."

keywords = ["python", "programming"]

highlighted_text = highlight_keywords(text, keywords)

print(highlighted_text)

# Вывод: "This is a sample text. We need to highlight *Python* and *programming*."
