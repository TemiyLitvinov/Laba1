import datetime


class Review:
    def __init__(self, id_review : int, student, course, rating : int, comment : str, date):
        self.id_review = id_review
        self.student = student
        self.course = course

        if not isinstance(rating, int) or not (1 <= rating <= 5):
            raise ValueError("Рейтинг должен быть целым числом от 1 до 5")

        self.rating = rating
        self.comment = comment
        self.date = date
        course.reviews.append(self)

    def edit_review(self, new_rating : int, new_comment : str):
        self.rating = new_rating
        self.comment = new_comment
        self.date = datetime.datetime.now()

    def get_summary(self) -> str:
        return (
            f'{self.student.fullname} о курсе "{self.course.title}:\n'
            f"Оценка {self.rating}/5\nКомментарий: {self.comment}"
            f"Дата: {self.date.strftime('%d.%m.%Y %H:%M')}"
        )