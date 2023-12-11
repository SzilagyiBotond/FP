from src.repository.grade_repository import GradeRepository
from src.domain.entities import Grade
from src.domain.validators import *
from src.domain.entities import *
from src.domain.dto import *
from src.repository.student_repository import StudentRepository
from src.repository.discipline_repository import DisciplineRepository


class GradeServices:
    def __init__(self, grade_repository, student_repository, discipline_repository):
        self.__grade_repository = grade_repository
        self.__student_repository = student_repository
        self.__discipline_repository = discipline_repository

    def add_grade(self, student_id, discipline_id, grade_value):
        grade = Grade(discipline_id, student_id, grade_value)
        self.__grade_repository.add(grade)

    def print_all_grades(self):
        # for grades in self.__grade_repository.find_all_grades():
        #     print(grades)
        return self.__grade_repository.find_all_grades()

    def delete_grades_associated_to_student(self, student_id):
        for grade in self.__grade_repository.find_all_grades():
            if grade.student_id == student_id:
                self.__grade_repository.delete_grade(grade)

    def delete_grades_associated_to_discipline(self, discipline_id):
        for grade in self.__grade_repository.find_all_grades():
            if grade.discipline_id == discipline_id:
                self.__grade_repository.delete_grade(grade)

    def calculate_averages_per_student_for_every_discipline(self):
        averages_per_student_and_discipline = []
        for student in self.__student_repository.find_all_students():
            for discipline in self.__discipline_repository.find_all_disciplines():
                grades = 0
                number_of_grades = 0
                for grade in self.__grade_repository.find_all_grades():
                    if grade.student_id == student.id and grade.discipline_id == discipline.id:
                        grades += grade.grade_value
                        number_of_grades += 1
                if number_of_grades > 0:
                    bukott_diak = StudentAverageDTO(student.id, discipline.id, grades / number_of_grades)
                    averages_per_student_and_discipline.append(bukott_diak)
        return averages_per_student_and_discipline

    def return_failing_students(self):
        averages_per_student_and_discipline = self.calculate_averages_per_student_for_every_discipline()
        failing_students = []
        for student in self.__student_repository.find_all_students():
            for average in averages_per_student_and_discipline:
                if average.student_id == student.id and average.average_grade_value < 4.5:
                    failing_students.append(student)
                    break
        return failing_students

    def calculate_aggregate_average_for_every_student(self):
        averages_per_student_and_discipline=self.calculate_averages_per_student_for_every_discipline()
        aggregate_averages_for_students=[]
        for student in self.__student_repository.find_all_students():
            discipline_averages=0
            number_of_disciplines=0
            for average in averages_per_student_and_discipline:
                if average.student_id==student.id:
                    discipline_averages +=average.average_grade_value
                    number_of_disciplines +=1
            if number_of_disciplines>0:
                aggregate_average=StudentGeneralAverageDTO(student.id,(discipline_averages/number_of_disciplines))
                aggregate_averages_for_students.append(aggregate_average)

        return aggregate_averages_for_students

    def sort_students_based_on_aggregate_average(self):
        aggregate_averages=self.calculate_aggregate_average_for_every_student()
        aggregate_averages.sort(key=lambda student:student.average_all,reverse=True)
        students_sorted=[]
        for student in aggregate_averages:
            students_sorted.append(self.__student_repository.find_by_id(student.student_id))
        return students_sorted

    def calculate_average_for_every_discipline(self):
        averages_per_student_and_discipline = self.calculate_averages_per_student_for_every_discipline()
        averages_per_discipline = []
        for discipline in self.__discipline_repository.find_all_disciplines():
            grades = 0
            number_of_grades = 0
            for average in averages_per_student_and_discipline:
                if average.discipline_id == discipline.id:
                    grades += average.average_grade_value
                    number_of_grades += 1
            if number_of_grades > 0:
                average_discipline = DisciplineAverageDTO(discipline.id, (grades / number_of_grades))
                averages_per_discipline.append(average_discipline)
        return averages_per_discipline

    def return_disciplines_sorted(self):
        discipline_averages = self.calculate_average_for_every_discipline()
        discipline_averages.sort(key=lambda discipline: discipline.average, reverse=True)
        best_disciplines = []
        for discipline in discipline_averages:
            best_disciplines.append(self.__discipline_repository.find_by_id(discipline.discipline_id))
        return best_disciplines


# discipline_validator
# student_validator=StudentValidator()
# student_repo=StudentRepository(student_validator)
# grade_validator = GradeValidator()
# grade_repo = GradeRepository(grade_validator)
# grade_serv = GradeServices(grade_repo)
