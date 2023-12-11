from src.domain.question import Question, QuestionValidator
from src.repository.MasterQuestions import MasterQuestions
from src.service.actions import GameActions
import unittest

class TestActions(unittest.TestCase):
    def setUp(self) -> None:
        self.validator=QuestionValidator()
        self.repo=MasterQuestions(self.validator,"test.txt")
        self.repo.generate_100_random_entries()
        self.action=GameActions(self.repo)

    def testAction(self):

        self.action.add_question(Question(101,"What",1,2,3,2,"medium"))
        quiz=self.action.create_quiz_in_memory("hard",10)
        self.assertIsNotNone(quiz,"Not okay")
        quiz=self.action.create_quiz_in_memory("essay",10)
        self.assertIsNone(quiz,"Not okay")
        self.action.create_quiz("easy",10,"test_easy.txt")
        self.action.create_quiz("medium",10,"test_medium.txt")
        self.repo.clear_master()
        quiz=self.action.create_quiz_in_memory("hard",200)
        self.assertIsNone(quiz,"Not okay")

