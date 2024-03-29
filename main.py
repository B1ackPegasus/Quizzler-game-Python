from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import Quiz_ui

question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui=Quiz_ui(quiz)  # wont work with whileloop near

#while quiz.still_has_questions():
   # quiz.next_question()


print(f"Your final score was: {quiz.score}/{quiz.question_number}")
