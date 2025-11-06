from datetime import datetime
from Review import Review


class Student:
    def __init__(self, id_student : int, fullname : str, email : str, password : str):
        self.id_student = id_student
        self.fullname = fullname
        self.email = email
        self.password = password
        self.enrolled_courses = []
        self.test_results = {}

    def enroll(self, course):
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)

    def take_test(self, test, answers: dict):
        result = test.evaluate(answers)
        self.test_results[test.id] = result
        return result

    def view_progress(self) -> float:
        if not self.test_results:
            return 0.0
        return round(sum(self.test_results.values()) / len(self.test_results), 2)

    def leave_review(self, course, rating: int, comment: str):
        if course not in self.enrolled_courses:
            print(f"{self.fullname} не записан на курс '{course.title}', отзыв невозможен.")
            return None
        id_review = len(course.reviews) + 1
        review = Review(id_review, self, course, rating, comment, datetime.now())
        course.reviews.append(review)
        print(f"Ваш отзыв о курсе оставлен")
        return review
