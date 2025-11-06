from Course import Course
from Student import Student
from Lesson import Lesson
from Test import Test
from Schedule import Schedule
from Review import Review


student = Student(1, "Петр Гринев", "petrg@gmail.com", "123454321")
course = Course(1, "Спидран к ЕГЭ", "Математика", "Сдашь матешу за 3 дня подготовки")
lesson1 = Lesson(1, "Квадратные уравнения", "https://Matesha.com/lesson1", "5 уравнений с конца вебинара", course)
lesson2 = Lesson(2, "Планиметрия 1-й части", "https://Matesha.com/lesson2", "10 номеров из пособия Ященко", course)
lesson3 = Lesson(3, "Стереометрия 1-й части", "https://Matesha.com/lesson3", "10 номеров из пособия Ященко", course)

course.add_lesson(lesson1)
course.add_lesson(lesson2)
student.enroll(course)
