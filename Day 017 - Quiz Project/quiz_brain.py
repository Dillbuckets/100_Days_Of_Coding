class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.user_score = 0

    # def next_question(game_continue, question_number, question_bank):
    #     if game_continue:
    #         question_number += 1
    #         current_question = question_bank[question_number]
    #         guess = input(f"Q.{question_number}: {current_question} (\"True\"/\"False\")?:").lower()
    #         return guess
    #     else:
    #         print("The game is over. You have lost.")

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            return True
        else: 
            return False


    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        guess = input(f"Q.{self.question_number}: {current_question.question_text} (True/False)?: ")
        self.check_answer(guess, current_question.answer)

    
    def check_answer(self, u_guess, c_question):
        if u_guess.lower() == c_question.lower():
            print("That is correct!")
            self.user_score += 1
        else:
            print("You got that one wrong.")
        print(f"The answer was: {u_guess}")
        print(f"Your current score is: {self.user_score}/{self.question_number}.")
        print("\n")
        