from datetime import datetime


class Schedule:
    def __init__(self, id_schedule, course, start_date: datetime, end_date: datetime):
        self.id_schedule = id_schedule
        self.course = course
        self.start_date = start_date
        self.end_date = end_date
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"Обучающийся {student.fullname} добавлен в расписание курса '{self.course.title}'.")
        else:
            print(f"Обучающийся {student.fullname} уже записан на этот курс.")

    def notify_students(self, lesson: str, lesson_time: datetime, video_url: str):
        print(f"Уведомление о начале урока '{lesson}' курса '{self.course.title}':")
        for student in self.students:
            print(f" - {student.fullname}, вебинар начинается {lesson_time.strftime('%d.%m.%Y %H:%M')}.")
            print(f"   Ссылка на урок: {video_url}\n")

    def get_schedule_info(self) -> str:
        return (
            f"Расписание #{self.id_schedule} для курса '{self.course.title}'\n"
            f"Дата начала курса: {self.start_date.strftime('%d.%m.%Y')}\n"
            f"Дата окончания курса: {self.end_date.strftime('%d.%m.%Y')}\n"
            f"Количество студентов: {len(self.students)}\n"
        )

    def __str__(self):
        return (
            f"Расписание #{self.id_schedule} — курс '{self.course.title}' "
            f"({self.start_date.strftime('%d.%m.%Y')}–{self.end_date.strftime('%d.%m.%Y')}, "
            f"студентов: {len(self.students)})"
        )
