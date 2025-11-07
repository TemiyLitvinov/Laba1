class Test:
    def __init__(self, id_test: int, title: str, max_score: float, course, questions: dict, correct_answers: dict):
        self.id_test = id_test
        self.title = title
        self.max_score = max_score
        self.course = course
        self.questions = questions
        self.correct_answers = correct_answers
        self.results = {}
        course.add_test(self)

    def evaluate(self, student_answers: dict) -> float:
        if not self.correct_answers:
            return 0.0
        score = 0
        for q, ans in student_answers.items():
            if q in self.correct_answers and ans == self.correct_answers[q]:
                score += self.max_score / len(self.correct_answers)
        return round(score, 2)

    def save_result(self, student, score: float):
        self.results[student.id_student] = score

    def get_result(self, student) -> float:
        return self.results.get(student.id_student, 0.0)
