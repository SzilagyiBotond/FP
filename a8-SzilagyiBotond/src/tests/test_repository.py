import unittest
from src.repository.discipline_repository import DisciplineRepository
from src.repository.student_repository import StudentRepository
from src.repository.grade_repository import GradeRepository
from src.domain.entities import *
from src.domain.validators import *


class StudentRepoTest(unittest.TestCase):
    def runTest(self):
        self.validator = StudentValidator()
        self.repository = StudentRepository(self.validator)
        self.repository.save(Student(1, "Robert"))
        self.assertEqual(self.repository.find_by_id(1), Student(1, "Robert"))
        self.assertEqual(self.repository.find_by_name("Robert"), [Student(1, "Robert")])
        self.repository.delete(Student(1, "Robert"))
        self.assertEqual(self.repository.find_by_id(1), None)
        self.repository.save(Student(1, "Robert"))
        self.repository.update(Student(1, "Boti"))
        self.assertEqual(self.repository.find_by_id(1), Student(1, "Boti"))


class DisciplineRepoTest(unittest.TestCase):

    def runTest(self):
        self.validator = DisciplineValidator()
        self.repository = DisciplineRepository(self.validator)
        self.repository.add(Discipline(1, "Math"))
        self.assertEqual(self.repository.find_by_id(1), Discipline(1, "Math"))
        self.repository.delete(Discipline(1, "Math"))
        self.assertEqual(self.repository.find_by_id(1), None)
        self.repository.add(Discipline(1, "Math"))
        self.repository.update(Discipline(1, "Mat"))
        self.assertEqual(self.repository.find_by_id(1), Discipline(1, "Mat"))


class GradeRepoTest(unittest.TestCase):

    def runTest(self):
        self.validator = GradeValidator()
        self.repository = GradeRepository(self.validator)
        self.repository.add(Grade(1, 1, 1))
        self.assertEqual(self.repository.find_all_grades(), [Grade(1, 1, 1)])
        self.repository.delete_grade(Grade(1, 1, 1))
        self.assertEqual(self.repository.find_all_grades(), [])
        self.repository.add(Grade(1, 1, 1))
        self.repository.update(Grade(1, 1, 2))
        self.assertEqual(self.repository.find_all_grades(), [Grade(1, 1, 2)])
