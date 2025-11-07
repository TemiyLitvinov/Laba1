from Exceptions import HomeworkError


class Lesson:
    def __init__(self, id_lesson: int, title: str, video_url: str, homework: str, course):
        self.id_lesson = id_lesson
        self.title = title
        self.video_url = video_url
        self.homework = homework
        self.course = course
        self.homework_answers = {}
        course.add_lesson(self)

    def go_to_lesson(self) -> str:
        if self.video_url:
            return f"Урок: {self.title}\nВидеоурок: {self.video_url}"
        return "Ссылка не работает."

    def submit_homework(self, student, answer: str) -> str:
        if not answer.strip():
            raise HomeworkError("Домашнее задание не может быть пустым.")
        self.homework_answers[student] = answer
        return "Ответ на домашнее задание отправлен."

    def __str__(self):
        return f"Урок: {self.title} (Ссылка: {self.video_url or 'нет'})"