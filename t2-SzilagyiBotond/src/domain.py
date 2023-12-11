from dataclasses import dataclass


@dataclass
class Assignment:
    __id: int
    __student_name: str
    __solution: str

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, new_id):
        self.__id = new_id

    @property
    def student_name(self):
        return self.__student_name

    @student_name.setter
    def student_name(self, new_student_name):
        self.__student_name = new_student_name

    @property
    def solution(self):
        return self.__solution

    @solution.setter
    def solution(self, new_solution):
        self.__solution = new_solution

    def __str__(self):
        return str(self.__id) + "," + str(self.__student_name) + "," + str(self.__solution)
