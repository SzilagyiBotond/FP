from src.domain.question import Question, QuestionValidator
import random


class RepoException(Exception):
    def __init__(self, message):
        self.__message = message

    def __str__(self):
        return self.__message


class MasterQuestions:
    def __init__(self, validator: QuestionValidator, file_name):
        self.__validator = validator
        self.__master_questions = {}
        self.__file_name = file_name
        self._load_file()

    def return_questions(self):
        """
        We return the list of questions
        :return:
        """
        return list(self.__master_questions.values())

    def add_question(self, question: Question):
        """
        We add a question to the master questions
        :param question:
        :return:
        """
        self.__validator.validate(question)
        if question.id in self.__master_questions.keys():
            raise RepoException("Invalid id")
        self.__master_questions[question.id] = question

    def _load_file(self):
        """
        We load the contents of tha file to the master questions
        :return:
        """
        with open(self.__file_name, "r") as content:
            for lines in content:
                question_to_parse = lines[:-1]
                question_to_parse = question_to_parse.split(";")
                question = Question(question_to_parse[0], question_to_parse[1], question_to_parse[2],
                                    question_to_parse[3], question_to_parse[4], question_to_parse[5],
                                    question_to_parse[6])
                self.add_question(question)
    def clear_master(self):
        self.__master_questions={}
        self.save_file()

    def save_file(self):
        """
        We save the questions in the master questions repo to a file
        :return:
        """
        with open(self.__file_name, "w") as f:
            for question in self.return_questions():
                to_add = str(question.id) + ";" + str(question.question) + ";" + str(question.answer_1) + ";" + str(
                    question.answer_2) + ";" + str(question.answer_3) + ";" + str(question.correct_answer) + ";" + str(
                    question.difficulty) + "\n"
                f.write(to_add)

    def generate_100_random_entries(self):
        """
        Generate 100 pseudo-random entry questions
        :return:
        """
        sample_simple_1="WHat is the biggest number?"
        sample_simple_2="What is the smallest number?"
        sample_medium_1="Which country has the largest GDP?"
        sample_medium_set_1=["China","Brazil","Canada","Romania","Switzerland","Uk"]
        sample_hard_1="How old am I?"
        sample_hard_set_1=[18,19,20,21,22,23,17]
        sample_simple_set_1=[1,2,3,4,5,6,7,8,9,10]
        sample_simple_set_2=[1,2,3,4,5,6,7,8,9,10]
        id=1
        for i in range(30):
            choices=random.sample(sample_simple_set_1,3)
            correct=max(choices[0],choices[1],choices[2])
            question=Question(id,sample_simple_1,choices[0],choices[1],choices[2],correct,"easy")
            self.add_question(question)
            id+=1
        for i in range(30):
            choices=random.sample(sample_simple_set_2,3)
            correct=min(choices[0],choices[1],choices[2])
            question=Question(id,sample_simple_2,choices[0],choices[1],choices[2],correct,"easy")
            self.add_question(question)
            id+=1
        for i in range(10):
            while True:
                choices=random.sample(sample_hard_set_1,3)
                correct=19
                if correct==choices[0] or choices[1]==correct or choices[2]==correct:
                    question = Question(id, sample_hard_1, choices[0], choices[1], choices[2], correct, "hard")
                    self.add_question(question)
                    break
            id+=1
        for i in range(30):
            choices=random.sample(sample_medium_set_1,3)
            if choices[0] == "Switzerland" or choices[1] == "Switzerland" or choices[2] == "Switzerland":
                correct="Switzerland"
            if choices[0]=="Canada" or choices[1]=="Canada" or choices[2]=="Canada":
                correct="Canada"
            if choices[0]=="Uk" or choices[1]=="Uk" or choices[2]=="Uk":
                correct="Uk"
            if choices[0] == "China" or choices[1] == "China" or choices[2] == "China":
                correct="China"
            question = Question(id, sample_medium_1, choices[0], choices[1], choices[2], correct, "medium")
            self.add_question(question)
            id+=1
        self.save_file()


# valid=QuestionValidator()
# repo=MasterQuestions(valid,"master.txt")
# repo.generate_100_random_entries()
# repo.save_file()
