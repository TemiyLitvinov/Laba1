class Lesson:
    def __init__(self, id_lesson : int, title : str, video_url : str, homework : str, course):
        self.id_lesson = id_lesson
        self.title = title
        self.video_url = video_url
        self.homework = homework
        self.course = course
        self.homework_answers = {}
        course.add_lesson(self)

    def go_to_lesson(self) -> str:
        if self.video_url:
            return f'Урок: {self.title}\nВидеоурок: {self.video_url}'
        else:
            return f'Ссылка не работает'

    def submit_homework(self, student, answer : str) -> str:
        self.homework_answers[student] = answer
        return "Ответ на домашнее задание отправлен"