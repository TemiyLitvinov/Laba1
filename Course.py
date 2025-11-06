class Course:
    def __init__(self, id_course : int, title : str, subject : str, description : str):
        self.id_course = id_course
        self.title = title
        self.subject = subject
        self.description = description
        self.lessons = []
        self.tests = []
        self.reviews = []

    def add_lesson(self, lesson):
        if lesson not in self.lessons:
            self.lessons.append(lesson)

    def add_test(self, test):
        if test not in self.tests:
            self.tests.append(test)

    def calculate_average_score(self):
        if not self.reviews:
            return 0.0
        return sum(r.rating for r in self.reviews) / len(self.reviews)

    def get_average_rating(self) -> float:
        if not self.reviews:
            return 0.0
        return sum(r.rating for r in self.reviews) / len(self.reviews)