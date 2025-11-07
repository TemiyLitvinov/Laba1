from json_read_write import read_json, write_json
from Review import Review
from datetime import datetime

def main():
    filename = "json_file.json"

    students = read_json(filename)
    if not students:
        print("Нет данных для чтения. Проверь файл json_file.json.")
        return

    student = students[0]
    print(f"\nСтудент: {student.fullname}")
    for course in student.enrolled_courses:
        print(f"Курс: {course.title} ({course.subject}) — {course.description}")
        for lesson in course.lessons:
            print(f"Урок: {lesson.title}")
        for review in course.reviews:
            print(f"Отзыв: {review.rating}/5 — {review.comment}")

    course = student.enrolled_courses[0]
    new_review = Review(
        id_review=len(course.reviews) + 1,
        student=student,
        course=course,
        rating=5,
        comment="Курс отличный! Всё понятно и доступно.",
        date=datetime.now()
    )
    course.reviews.append(new_review)
    print("\nДобавлен новый отзыв к курсу.")

    write_json(filename, students)


if __name__ == "__main__":
    main()
