from Course import Course
from Student import Student
from Lesson import Lesson
from Test import Test
from Schedule import Schedule
from datetime import datetime
from datetime import timedelta


student = Student(1, "Петр Гринев", "petrg@gmail.com", "123454321")
course = Course(1, "Спидран подготовка к ЕГЭ за 3 дня", "Математика", "Сдашь матешу за 3 дня подготовки")
lesson1 = Lesson(1, "Квадратные уравнения", "https://Matesha.com/lesson1", "1 уравнение с конца вебинара", course)
lesson2 = Lesson(2, "Планиметрия 1-й части", "https://Matesha.com/lesson2", "1 номер из пособия Ященко", course)
lesson3 = Lesson(3, "Стереометрия 1-й части", "https://Matesha.com/lesson3", "1 номер из пособия Ященко", course)

course.add_lesson(lesson1)
course.add_lesson(lesson2)

student.enroll(course)

print(lesson1.go_to_lesson())
print(lesson1.submit_homework(student, "Решения отправлены!"))

questions = {
    1: "Корни уравнения x ^ 2 - 4 = 0?",
    2: "Площадь квадрата со стороной 3?",
    3: "Сколько граней у куба?"
}
correct_answers = {1: "+-2", 2: "9", 3: "6"}

test1 = Test(1, "Математика: основы", 3, course, questions, correct_answers)
course.add_test(test1)

student_answers = {1: "2", 2: "9", 3: "6"}
score = student.take_test(test1, student_answers)
test1.save_result(student, score)
print(f"\nРезультат теста '{test1.title}': {score}/{test1.max_score}")
print(f"Сохранённый результат: {test1.get_result(student)}")


print(f"Прогресс студента: {student.view_progress()}%")

review = student.leave_review(course, 5, "Отличный курс, всё очень понятно!")
if review:
    print(review.get_summary())
review.edit_review(4, "Хорошо, но хотелось бы больше практики.")

print(review.get_summary())

# Средний рейтинг курса
print(f"\nСредний рейтинг курса '{course.title}': {course.get_average_rating():.2f}/5")

schedule = Schedule(1, course, start_date=datetime.now(), end_date=datetime.now() + timedelta(days=3))
schedule.add_student(student)
# Информация о расписании
print(schedule.get_schedule_info())

schedule.notify_students(
    lesson="Квадратные уравнения",
    lesson_time=datetime.now() + timedelta(hours=1),
    video_url="https://Matesha.com/lesson1"
)