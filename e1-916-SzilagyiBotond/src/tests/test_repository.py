from src.domain.question import Question, QuestionValidator
from src.repository.MasterQuestions import MasterQuestions

import unittest


class TestRepo(unittest.TestCase):
    def setUp(self) -> None:
        self.validator = QuestionValidator()
        self.repository = MasterQuestions(self.validator,"test.txt")
        self.repository.generate_100_random_entries()

    def testRepo(self):
        self.assertEqual(len(self.repository.return_questions()),100)
        self.repository.add_question(Question(101,"What",1,2,3,2,"hard"))
        self.assertEqual(len(self.repository.return_questions()),101)
        self.assertEqual(self.repository.return_questions()[-1].difficulty,"hard")
        self.assertEqual(self.repository.return_questions()[-1].id,101)
        self.repository.clear_master()
        self.assertEqual(len(self.repository.return_questions()),0)


