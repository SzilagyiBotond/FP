from src.services.grade_services import GradeServices
from src.services.student_services import StudentServices
from src.services.discipline_services import DisciplineServices
from src.repository.repository_exceptions import RepositoryExceptions
from src.repository.student_repository import StudentRepository
from src.repository.discipline_repository import DisciplineRepository
from src.repository.grade_repository import GradeRepository
from src.domain.validators import *
from src.domain.entities import *
from src.services.service_exceptions import ServiceExceptions


class Console:
    def __init__(self, grade_service, student_service, discipline_service):
        self.__grade_service = grade_service
        self.__student_service = student_service
        self.__discipline_service = discipline_service

    def add_student(self):
        try:
            id = int(input("What id should he have: "))
            name = input("What is the name: ")
            self.__student_service.add_student(id, name)
        except RepositoryExceptions or ValueError as re:
            print(re)

    def delete_student(self):
        try:
            id = int(input("What id: "))

            self.__student_service.delete_student(id)
            self.__grade_service.delete_grades_associated_to_student(id)
        except ServiceExceptions as re:
            print(re)

    def update_student(self):
        try:
            id = int(input("What id: "))
            name = input("What is the new name: ")
            self.__student_service.update_student(id, name)
        except ServiceExceptions as re:
            print(re)

    def print_all_student(self):
        try:
            for students in self.__student_service.list_all_student():
                print(students)
        except RepositoryExceptions or ValueError as re:
            print(re)

    def print_all_disciplines(self):
        for discipline in self.__discipline_service.list_all_discipline():
            print(discipline)

    def add_discipline(self):
        try:
            id = int(input("What should be the id: "))
            name = input("What should be the name: ")
            self.__discipline_service.add_discipline(id, name)
        except RepositoryExceptions or ValueError as re:
            print(re)

    def delete_discipline(self):
        try:
            id = int(input("What is the id: "))
            self.__discipline_service.delete_discipline(id)
            self.__grade_service.delete_grades_associated_to_discipline(id)
        except ServiceExceptions as re:
            print(re)

    def update_discipline(self):
        try:
            id = int(input("What is the id: "))
            name = input("What is the new name: ")
            self.__discipline_service.update_discipline(id, name)
        except ServiceExceptions as re:
            print(re)

    def print_failing_pupils(self):
        for student in self.__grade_service.return_failing_students():
            print(student)

    def print_disciplines_sorted(self):
        for discipline in self.__grade_service.return_disciplines_sorted():
            print(discipline)
        # for averages in self.__grade_service.calculate_average_for_every_discipline():
        #     print(averages)

    def print_students_sorted(self):
        for student in self.__grade_service.sort_students_based_on_aggregate_average():
            print(student)

    def add_grade(self):
        try:
            student = int(input("What is the student's id: "))
            discipline = int(input("What is the discipline's id: "))
            grade_value = int(input("What is the grade: "))
            self.__student_service.find_student_by_id(student)
            self.__discipline_service.find_discipline_by_id(discipline)
            self.__grade_service.add_grade(student, discipline, grade_value)
        except ServiceExceptions as se:
            print(se)

    def find_students_or_disciplines(self):
        try:
            command_1 = int(input("Press 1-Search for a student or 2-Search for a discipline: "))
            if command_1 == 1:
                command_2 = int(input("Press 1-search by name or 2-search by id: "))
                # command_3 = input("Enter the property: ")
                # search_student = {"1": self.__student_service.find_student_by_name,
                #                   "2": self.__student_service.find_student_by_id}
                # search_student[command_2](str(command_3))
                if command_2 == 1:
                    command_3 = input("Enter the property: ")
                    self.__student_service.find_student_by_name(command_3)
                if command_2 == 2:
                    command_3 = int(input("Enter the property: "))
                    self.__student_service.find_student_by_id(command_3)
            if command_1 == 2:
                command_2 = int(input("Press 1-search by name or 2-search by id: "))
                # command_3 = (input("Enter the property: "))
                # search_discipline = {"1": self.__discipline_service.find_discipline_by_name,
                #                      "2": self.__discipline_service.find_discipline_by_id}
                # search_discipline[command_2](command_3)
                if command_2 == 1:
                    command_3 = input("Enter the property: ")
                    for discipline in self.__discipline_service.find_discipline_by_name(command_3):
                        print(discipline)
                if command_2 == 2:
                    command_3 = int(input("Enter the property: "))
                    print(self.__discipline_service.find_discipline_by_id(command_3))
        except ValueError as ve:
            print(ve)
        except ServiceExceptions as se:
            print(se)

    def list_all_grades(self):
        for grade in self.__grade_service.print_all_grades():
            print(grade)

    def print_options(self):
        print("1. Manage students")
        print("2. Manage disciplines")
        print("3. Add grade")
        print("4. Display all grades")
        print("5. Search discipline or student")
        print("6. Display failing students")
        print("7. Students sorted by aggregate average")
        print("8. Disciplines sorted by average")
        print("9. Exit")

    def print_options_for_students(self):
        print("1. Add student")
        print("2. Remove student")
        print("3. Update student")
        print("4. List all students")

    def print_options_for_disciplines(self):
        print("1. Add discipline")
        print("2. Remove discipline")
        print("3. Update discipline")
        print("4. List all disciplines")

    def generate_10_entries(self):
        self.__student_service.add_student(1, "Szilagyi Botond")
        self.__student_service.add_student(2, "Janos Akos-Marton")
        self.__student_service.add_student(3, "Lazar Robert")
        self.__student_service.add_student(4, "Beno Akos")
        self.__student_service.add_student(5, "Reman Attila")
        self.__student_service.add_student(6, "Adorjani Bence")
        self.__student_service.add_student(7, "Schuller Abigel")
        self.__student_service.add_student(8, "Kiss Orsolya")
        self.__student_service.add_student(9, "Kovacs Robert")
        self.__student_service.add_student(10, "Pentek Mark")
        self.__discipline_service.add_discipline(1, "Matek")
        self.__discipline_service.add_discipline(2, "Physics")
        self.__discipline_service.add_discipline(3, "Magyar")
        self.__discipline_service.add_discipline(4, "Informatika")
        self.__grade_service.add_grade(1, 1, 10)
        self.__grade_service.add_grade(2, 1, 9)
        self.__grade_service.add_grade(3, 1, 8)
        self.__grade_service.add_grade(4, 1, 7)
        self.__grade_service.add_grade(5, 1, 6)
        self.__grade_service.add_grade(6, 1, 5)
        self.__grade_service.add_grade(7, 1, 4)
        self.__grade_service.add_grade(8, 1, 3)
        self.__grade_service.add_grade(9, 1, 2)
        self.__grade_service.add_grade(10, 1, 1)
        self.__grade_service.add_grade(1, 2, 10)
        self.__grade_service.add_grade(2, 2, 9)
        self.__grade_service.add_grade(3, 2, 8)
        self.__grade_service.add_grade(4, 2, 7)
        self.__grade_service.add_grade(5, 2, 6)
        self.__grade_service.add_grade(6, 2, 5)
        self.__grade_service.add_grade(7, 2, 4)
        self.__grade_service.add_grade(8, 2, 3)
        self.__grade_service.add_grade(9, 2, 2)
        self.__grade_service.add_grade(10, 2, 1)
        self.__grade_service.add_grade(1, 3, 10)
        self.__grade_service.add_grade(2, 3, 9)
        self.__grade_service.add_grade(3, 3, 8)
        self.__grade_service.add_grade(4, 3, 7)
        self.__grade_service.add_grade(5, 3, 6)
        self.__grade_service.add_grade(6, 3, 5)
        self.__grade_service.add_grade(7, 3, 4)
        self.__grade_service.add_grade(8, 3, 3)
        self.__grade_service.add_grade(9, 3, 2)
        self.__grade_service.add_grade(10, 3, 1)
        self.__grade_service.add_grade(1, 4, 10)
        self.__grade_service.add_grade(2, 4, 9)
        self.__grade_service.add_grade(3, 4, 8)
        self.__grade_service.add_grade(4, 4, 7)
        self.__grade_service.add_grade(5, 4, 6)
        self.__grade_service.add_grade(6, 4, 5)
        self.__grade_service.add_grade(7, 4, 4)
        self.__grade_service.add_grade(8, 4, 3)
        self.__grade_service.add_grade(9, 4, 2)
        self.__grade_service.add_grade(10, 4, 1)

    def run_console(self):
        options_for_students = {"1": self.add_student, "2": self.delete_student, "3": self.update_student,
                                "4": self.print_all_student}
        options_for_disciplines = {"1": self.add_discipline, "2": self.delete_discipline, "3": self.update_discipline,
                                   "4": self.print_all_disciplines}
        other_options_besides_the_student_and_discipline_management = {"5":self.find_students_or_disciplines ,"6": self.print_failing_pupils,
                                                                       "7": self.print_students_sorted,
                                                                       "8": self.print_disciplines_sorted,
                                                                       "3": self.add_grade, "4": self.list_all_grades}
        self.generate_10_entries()
        while True:
            self.print_options()
            command = int(input(">"))
            if command == 1:
                self.print_options_for_students()
                student_command = input(">")
                options_for_students[student_command]()
            if command == 2:
                self.print_options_for_disciplines()
                discipline_command = input(">")
                options_for_disciplines[discipline_command]()
            if command == 9:
                break
            else:
                if str(command) in other_options_besides_the_student_and_discipline_management:
                    other_options_besides_the_student_and_discipline_management[str(command)]()
            # if command == 3:
            #     self.add_grade()
            # if command == 4:
            #     self.list_all_grades()
            # if command == 5:
            #     self.find_students_or_disciplines()
            # if command == 6:
            #     self.print_failing_pupils()
            # if command == 8:
            #     self.print_disciplines_sorted()
            # if command == 9:
            #     self.print_students_sorted()

# stud_repo = StudentRepository(StudentValidator())
# stud_service = StudentServices(stud_repo)
# disc_repo = DisciplineRepository(DisciplineValidator())
# disc_services = DisciplineServices(disc_repo)
# grade_repo = GradeRepository(GradeValidator())
# grade_services = GradeServices(grade_repo, stud_repo, disc_repo)
# console = Console(grade_services, stud_service, disc_services)
# console.run_console()
