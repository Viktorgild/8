class ExceptionClass:
    def __init__(self, divider, denominator):
        self.divider = divider
        self.denominator = denominator

    @staticmethod
    def divide_by_null(divider, denominator):
        try:
            return (divider / denominator)
        except:
            return (f"Деление на ноль недопустимо")


div = ExceptionClass(10, 100)
print(ExceptionClass.divide_by_null(10, 0))
print(ExceptionClass.divide_by_null(10, 0.1))
print(div.divide_by_null(100, 0))
