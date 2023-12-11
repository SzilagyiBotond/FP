class Question:
    def __init__(self, id, question, answer_1, answer_2, answer_3, correct_answer, difficulty):
        self.__id = id
        self.__question = question
        self.__answer_1 = answer_1
        self.__answer_2 = answer_2
        self.__answer_3 = answer_3
        self.__correct_answer = correct_answer
        self.__difficulty = difficulty

    @property
    def id(self):
        return self.__id

    @property
    def question(self):
        return self.__question

    @property
    def answer_1(self):
        return self.__answer_1

    @property
    def answer_2(self):
        return self.__answer_2

    @property
    def answer_3(self):
        return self.__answer_3

    @property
    def correct_answer(self):
        return self.__correct_answer

    @property
    def difficulty(self):
        return self.__difficulty

    def __str__(self):
        return str(self.__question) + "\n" + str(self.__answer_1) + "\n" + str(self.__answer_2) + "\n" + str(
            self.__answer_3)


class TypeException(Exception):
    def __init__(self, message):
        self.message = message

    def __str__(self):
        return self.message


class QuestionValidator:
    def validate(self, question: Question):
        if question.question == "" or question.answer_1 == "" or question.answer_3 == "" or question.answer_2 == "" or question.correct_answer == "":
            raise TypeException("Not valid input")
        if question.difficulty != "easy" and question.difficulty != "hard" and question.difficulty != "medium":
            raise TypeException("Not valid input")
