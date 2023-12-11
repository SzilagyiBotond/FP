from src.domain.question import Question, QuestionValidator
from src.repository.MasterQuestions import *
import random





class GameActions:
    def __init__(self, master_questions: MasterQuestions):
        self.__master_questions = master_questions

    def count_question_types(self):
        """
        We count the number of each question type - easy,medium,hard
        :return:
        """
        types = [0, 0, 0]
        for question in self.__master_questions.return_questions():
            if question.difficulty == "easy":
                types[0] += 1

            if question.difficulty == "medium":
                types[1] += 1
            if question.difficulty == "hard":
                types[2] += 1

        return types

    def clear_master(self):
        """
        This function erases all questions from the master questions
        :return:
        """
        self.__master_questions.clear_master()
    def create_quiz_in_memory(self, difficulty, number_of_questions):
        """
        Create a quiz based on the difficulty level and the number of questions, which in the create_quiz method is used
        :param difficulty:
        :param number_of_questions:
        :return:
        """
        types = self.count_question_types()
        if difficulty == "easy":
            if number_of_questions // 2 > types[0]:
                raise RepoException("Cannot create quiz")
            while True:
                possible_question = random.sample(self.__master_questions.return_questions(), number_of_questions)
                easy_question = 0
                for question in possible_question:
                    if question.difficulty == "easy":
                        easy_question += 1
                if easy_question >=  number_of_questions // 2:
                    return possible_question
        if difficulty == "medium":
            if number_of_questions // 2 > types[1]:
                raise RepoException("Cannot create quiz")
            while True:
                possible_question = random.sample(self.__master_questions.return_questions(), number_of_questions)
                medium_question = 0
                for question in possible_question:
                    if question.difficulty == "medium":
                        medium_question += 1
                if medium_question >= number_of_questions // 2:
                    return possible_question
        if difficulty == "hard":
            if number_of_questions // 2 > types[2]:
                raise RepoException("Cannot create quiz")
            while True:
                possible_question = random.sample(self.__master_questions.return_questions(), number_of_questions)
                hard_question = 0
                for question in possible_question:
                    if question.difficulty == "hard":
                        hard_question += 1
                if hard_question >= number_of_questions // 2:
                    return possible_question

    def create_quiz(self, difficulty, number_of_questions, file_name):
        """
        We create a quiz, and store it in a file, with respect to the given attributes, such as filename,difficulty, number of questions.
        :param difficulty:
        :param number_of_questions:
        :param file_name:
        :return:
        """
        quiz = self.create_quiz_in_memory(difficulty, number_of_questions)
        with open(file_name, "w") as f:
            for question in quiz:
                to_add = str(question.id) + ";" + str(question.question) + ";" + str(question.answer_1) + ";" + str(
                    question.answer_2) + ";" + str(question.answer_3) + ";" + str(question.correct_answer) + ";" + str(
                    question.difficulty) + "\n"
                f.write(to_add)

    def return_quiz(self, file_name):
        """
        This function returns the quiz located at the file_name
        :param file_name:
        :return:
        """
        quiz = []
        with open(file_name, "r") as content:
            for line in content:
                question_to_parse = line[:-1]
                question_to_parse = question_to_parse.split(";")
                question = Question(question_to_parse[0], question_to_parse[1], question_to_parse[2],
                                    question_to_parse[3], question_to_parse[4], question_to_parse[5],
                                    question_to_parse[6])
                quiz.append(question)
        return quiz

    def add_question(self, question):
        self.__master_questions.add_question(question)
        self.__master_questions.save_file()

class GameException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message