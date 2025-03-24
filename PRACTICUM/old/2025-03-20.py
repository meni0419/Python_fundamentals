def generator_123():
    for i in range(1, 4):
        yield i

numbers = list(generator_123())
print(numbers)

def my_generator():
    print("Начало")
    yield 1
    print("После первого yield")
    yield 2
    print("После второго yield")
    yield 3
    print("Завершение")

gen = my_generator()

# Используем генератор
print(next(gen))  # Начало, вернет 1
print(next(gen))  # После первого yield, вернет 2
print(next(gen))  # После второго yield, вернет 3
