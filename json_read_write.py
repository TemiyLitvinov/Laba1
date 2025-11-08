import json
from datetime import datetime
from Student import Student
from Course import Course
from Lesson import Lesson
from Review import Review


def read_json(filename: str):
    students = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)

        for s in data.get("students", []):
            student = Student(
                id_student=s["id_student"],
                fullname=s["fullname"],
                email=s["email"],
                password=s["password"]
            )

            for c in s.get("enrolled_courses", []):
                course = Course(
                    id_course=c["id_course"],
                    title=c["title"],
                    subject=c["subject"],
                    description=c["description"]
                )

                for l in c.get("lessons", []):
                    lesson = Lesson(
                        id_lesson=l["id_lesson"],
                        title=l["title"],
                        video_url=l["video_url"],
                        homework=l["homework"],
                        course=course
                    )
                    lesson.homework_answers = l.get("homework_answers", {})

                for r in c.get("reviews", []):
                    review = Review(
                        id_review=r["id_review"],
                        student=student,
                        course=course,
                        rating=r["rating"],
                        comment=r["comment"],
                        date=datetime.fromisoformat(r["date"])
                    )
                    course.reviews.append(review)

                student.enrolled_courses.append(course)

            student.test_results = s.get("test_results", {})

            students.append(student)

        print(f"Из файла '{filename}' загружено {len(students)} студентов.")
        return students

    except FileNotFoundError:
        print(f"Файл '{filename}' не найден.")
        return []
    except json.JSONDecodeError:
        print(f"Ошибка формата JSON в '{filename}'.")
        return []
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
        return []


def write_json(filename: str, students: list):
    try:
        data = {
            "students": []
        }

        for s in students:
            student_data = {
                "id_student": s.id_student,
                "fullname": s.fullname,
                "email": s.email,
                "password": s.password,
                "enrolled_courses": [],
                "test_results": s.test_results
            }

            for c in s.enrolled_courses:
                course_data = {
                    "id_course": c.id_course,
                    "title": c.title,
                    "subject": c.subject,
                    "description": c.description,
                    "lessons": [],
                    "tests": [],
                    "reviews": []
                }

                for l in c.lessons:
                    course_data["lessons"].append({
                        "id_lesson": l.id_lesson,
                        "title": l.title,
                        "video_url": l.video_url,
                        "homework": l.homework,
                        "homework_answers": l.homework_answers
                    })

                for r in c.reviews:
                    course_data["reviews"].append({
                        "id_review": r.id_review,
                        "student": {
                            "id_student": r.student.id_student,
                            "fullname": r.student.fullname
                        },
                        "rating": r.rating,
                        "comment": r.comment,
                        "date": r.date.isoformat()
                    })

                student_data["enrolled_courses"].append(course_data)

            data["students"].append(student_data)

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        print(f"Данные успешно сохранены в файл '{filename}'")

    except Exception as e:
        print(f"Ошибка при сохранении данных: {e}")