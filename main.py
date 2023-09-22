
from questions import questions

class Question:
    def __init__(self, question_text, correct_answer):
        self.question_text = question_text
        self.correct_answer = correct_answer

    def check_answer(self, user_answer):
        return user_answer.lower() == self.correct_answer.lower()

class Quiz:
    def __init__(self):
        self.questions = [Question(q["text"], q["answer"]) for q in questions]
        self.score = 0
        self.current_question_index = 0

    def next_question(self):
        if self.current_question_index < len(self.questions):
            return self.questions[self.current_question_index]
        else:
            return None

    def take_quiz(self):
        while self.next_question():
            current_question = self.next_question()
            print(f"Question: {current_question.question_text}")
            user_answer = input("Your answer (True/False): ")
            if current_question.check_answer(user_answer):
                print("Correct! You earned 2 points.")
                self.score += 2
            else:
                print("Wrong! You lost 1 point.")
                self.score -= 1
            self.current_question_index += 1

        self.display_score()

    def display_score(self):
        print(f"Your final score is: {self.score}")

if __name__ == "__main__":
    quiz = Quiz()
    print("Welcome to the Python Quiz!")
    quiz.take_quiz()
