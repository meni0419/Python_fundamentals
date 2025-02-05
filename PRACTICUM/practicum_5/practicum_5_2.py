def price_in_euro_p5_1(product, price):
    """Напишите программу, которая печатает ценник по параметрам: “The price of <product> is “X” Euro”.
    В строке <product> и <X> - параметры. Убедитесь, что цена выводится в Евро с центами (не более двух знаков после запятой).
    """
    print(f"The price of {product} is {price:.2f} euro")


product_p5_1 = "pineapple"
price_p5_1 = 1.265467

price_in_euro_p5_1(product_p5_1, price_p5_1)
