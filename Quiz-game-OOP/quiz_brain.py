class QuizBrain:
    def __init__(self, question_list):
        self.score = 0
        self.qlist = question_list
        self.qnumber = 0

    def still_has_question(self):
        return self.qnumber < len(self.qlist)

    def next_question(self):
        current_question = self.qlist[self.qnumber]
        self.qnumber += 1
        user_answer = input(f"Q.{self.qnumber}:{current_question.text}. (True/False)?:")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right✔️✔️✔️")
        else:
            print("You got it wrong.❌")
        print(f"the correct answer was: {correct_answer}")
        print(f"Current Score: {self.score}/{self.qnumber}")
        print("\n")
