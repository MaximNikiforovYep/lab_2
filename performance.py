class Performance:
    def __init__(self, student, course):
        self.student = student
        self.course = course

    def get_performance_report(self) -> str:
        avg_grade = self.student.average_grade()
        discount = self.course.calculate_discount(avg_grade)
        discounted_price = self.course.discounted_price(avg_grade)

        report = (
            f"Студент: {self.student.name}\n"
            f"Средняя оценка: {avg_grade:.2f}\n"
            f"Курс: {self.course.title}\n"
            f"Цена курса без скидки: {self.course.price} руб.\n"
            f"Скидка: {discount * 100}%\n"
            f"Цена курса со скидкой: {discounted_price} руб.\n"
        )
        return report