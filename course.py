class Course:
    def __init__(self, title: str, price: float):
        self.title = title
        self.price = price

    def calculate_discount(self, average_grade: float) -> float:
        if average_grade >= 90:
            return 0.3  # скидка 30%
        elif average_grade >= 75:
            return 0.2
        elif average_grade >= 60:
            return 0.1
        else:
            return 0.0

    def discounted_price(self, average_grade: float) -> float:
        discount = self.calculate_discount(average_grade)
        return self.price * (1 - discount)