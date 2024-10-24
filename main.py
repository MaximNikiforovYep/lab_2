from student import Student
from course import Course
from performance import Performance
from docx import Document


def save_report_to_doc(report: str, filename: str = "report.docx"):
    doc = Document()
    doc.add_paragraph(report)
    doc.save(filename)
    print(f"Отчет сохранен в {filename}")


def main():
    student_name = input("Введите имя студента: ")
    course_title = input("Введите название курса: ")
    course_price = float(input("Введите цену курса (руб.): "))

    student = Student(student_name)
    course = Course(course_title, course_price)

    while True:
        try:
            grade = float(input("Введите оценку студента (или 'q' для выхода): "))
            student.add_grade(grade)
        except ValueError:
            break

    performance = Performance(student, course)
    report = performance.get_performance_report()
    print("\nРезультаты успеваемости и скидки на курс:")
    print(report)

    save_to_doc = input("Хотите сохранить отчет в файл (да/нет)? ").lower()
    if save_to_doc == 'да':
        filename = input("Введите имя файла (например, report.docx): ")
        save_report_to_doc(report, filename)


if __name__ == "__main__":
    main()