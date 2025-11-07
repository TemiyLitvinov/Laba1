from datetime import datetime
from Exceptions import ReviewError


class Review:
    def __init__(self, id_review: int, student, course, rating: int, comment: str, date):
        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ReviewError("Рейтинг должен быть целым числом от 1 до 5.")

        self.id_review = id_review
        self.student = student
        self.course = course
        self.rating = rating
        self.comment = comment
        self.date = date
        course.reviews.append(self)

    def edit_review(self, new_rating: int, new_comment: str):
        if not isinstance(new_rating, int) or not (1 <= new_rating <= 5):
            raise ReviewError("Рейтинг должен быть от 1 до 5.")
        self.rating = new_rating
        self.comment = new_comment
        self.date = datetime.now()

    def get_summary(self) -> str:
        return (
            f"{self.student.fullname} о курсе \"{self.course.title}\":\n"
            f"Оценка {self.rating}/5\nКомментарий: {self.comment}\n"
            f"Дата: {self.date.strftime('%d.%m.%Y %H:%M')}\n"
        )

    def __str__(self):
        return (
            f"Отзыв от {self.student.fullname}: {self.rating}/5 — {self.comment}"
            f" ({self.date.strftime('%d.%m.%Y')})"
        )