import unittest
from src.domain import Assignment
from src.repository import HomeworksFile

class TestAdd(unittest.TestCase):
    def runTest(self):
        self.repo=HomeworksFile("Input.txt")
        self.repo.add_assignment(Assignment(6,"ADa","Nothing"))
        self.assertEqual(self.repo.return_assignments()[5],Assignment(6,"ADa","Nothing"),"Not okay")
        self.repo.add_assignment(Assignment(7,"Bean","Oh yes"))