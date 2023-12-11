from src.domain import Assignment
from src.repository import HomeworksFile
from src.services import AssignmentServices

class UI:
    def __init__(self,assignment_services:AssignmentServices):
        self.__assignment_service=assignment_services

    def add_student(self):
        try:
            id=int(input("What id: "))
            name=input("What name: ")
            solution=input("What solution: ")
            self.__assignment_service.add_assignment(id,name,solution)
        except ValueError as ve:
            print(ve)
    def print_all_assignments(self):
        for assignment in self.__assignment_service.list_all_assignments():
            print(assignment)

    def dishonest_check(self):
        for dishonest_pairs in self.__assignment_service.dishonesty_check():
            print(*dishonest_pairs)

    def print_options(self):
        print("1.Add a student")
        print("2.Display the students")
        print("3.Dishonesty check")
        print("4. Exit")

    def run_console(self):
        while True:
            try:
                self.print_options()
                command=int(input("What should I do for you: "))
                if command==1:
                    self.add_student()
                if command==2:
                    self.print_all_assignments()
                if command==3:
                    self.dishonest_check()
                if command==4:
                    break
            except ValueError as ve:
                print(ve)


repo=HomeworksFile("input.txt")
service=AssignmentServices(repo)
console=UI(service)
console.run_console()
