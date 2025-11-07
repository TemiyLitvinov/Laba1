class EnrollmentError(Exception):
    def __init__(self, message="Не удалось записать студента на курс."):
        super().__init__(message)


class ReviewError(Exception):
    def __init__(self, message="Ошибка при работе с отзывом."):
        super().__init__(message)


class TestError(Exception):
    def __init__(self, message="Ошибка при работе с тестом."):
        super().__init__(message)


class HomeworkError(Exception):
    def __init__(self, message="Ошибка при отправке домашнего задания."):
        super().__init__(message)