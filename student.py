class Student:
    def __init__(self, name: str):
        self.name = name
        self.grades = []

    def add_grade(self, grade: float):
        self.grades.append(grade)

    def average_grade(self) -> float:
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)