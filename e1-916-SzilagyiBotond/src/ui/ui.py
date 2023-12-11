from src.service.actions import *
from src.domain.question import *
from src.repository.MasterQuestions import *


# FileNotFoundError
class UiException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class Ui:
    def __init__(self, actions: GameActions):
        self.__actions = actions

    @staticmethod
    def print_options():
        print(
            "add - add a question to the master list of questions - correct format: add <id>;<text>;<choice_a>;<choice_b>;<choice_c>;<correct_choice>;<difficulty>")
        print("create - create a quiz - correct format: create <difficulty> <number_of_questions> <file>")
        print("start - start a quiz - correct format: start <file>")
        print("exit")

    def add_question(self, question_string: str):
        try:
            to_add = question_string.split(";")
            if len(to_add) != 7:
                raise UiException("Not correct input")
            question = Question(int(to_add[0]), to_add[1], to_add[2], to_add[3], to_add[4], to_add[5], to_add[6])
            self.__actions.add_question(question)
        except UiException as ui:
            print(ui)
        except TypeException as te:
            print(te)
        except RepoException as re:
            print(re)

    def create_quiz(self, difficulty, number_of_questions, file):
        try:
            if difficulty != "easy" and difficulty != "medium" and difficulty != "hard":
                raise UiException("Not valid difficulty")
            self.__actions.create_quiz(difficulty, number_of_questions, file)

        except UiException as ui:
            print(ui)
        except RepoException as ge:
            print(ge)

    def start_quiz(self, file):
        try:
            quiz = self.__actions.return_quiz(file)
            points = 0
            for question in quiz:
                print(question)
                answer = input("What is the answer: ")
                if answer == question.correct_answer:
                    if question.difficulty == "easy":
                        points += 1
                    if question.difficulty == "medium":
                        points += 2
                    if question.difficulty == "hard":
                        points += 3
            print("You got: ", points, " points")
        except FileNotFoundError as fe:
            print(fe)

    def run_console(self):
        while True:
            try:
                self.print_options()
                command = input("What to do: ")
                blank = command.find(" ")
                if command[:blank] == "add":
                    self.add_question(command[blank + 1:])
                command = command.split(" ")
                if command[0] == "exit" and len(command) == 1:
                    self.__actions.clear_master()
                    break
                elif command[0] == "create" and len(command) == 4:
                    self.create_quiz(command[1], int(command[2]), command[3])
                elif command[0] == "start" and len(command) == 2:
                    self.start_quiz(command[1])
                elif command[0]!="add":
                    print("Invalid input")
            except ValueError as ve:
                print(ve)
