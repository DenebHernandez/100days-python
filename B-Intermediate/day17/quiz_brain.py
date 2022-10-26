
class QuizBrain():

    def __init__(self, question_list) -> None:
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def next_question(self):
        current_question =  self.question_list[self.question_number]
        current_text = current_question.text
        current_answer = current_question.answer
        user_answer = input(f"Q.{self.question_number + 1}: {current_text} (True/False)?: ")
        self.check_anser(user_answer=user_answer, current_answer=current_answer)
        self.question_number += 1


    def still_has_questions(self):
        list_len = len(self.question_list)
        return self.question_number < list_len


    def check_anser(self, user_answer, current_answer):
        if current_answer.lower() == user_answer.lower():
            self.score += 1
            print("You got it right!")
        else:
            print(f"You got it wrong. The answer was {current_answer}.")
        print(f"Your score is {self.score}/{self.question_number + 1}.")
