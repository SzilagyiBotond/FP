from src.domain import Assignment


class HomeworksFile():
    def __init__(self, file_name):
        self.__assignments = {}
        self.__file_name = file_name
        self._load_file()

    def add_assignment(self, assignment):
        if assignment.id not in self.__assignments and assignment.solution!="":
            self.__assignments[assignment.id] = assignment
        else:
            raise ValueError("Ïnvalid input")

    def return_assignments(self):
        return list(self.__assignments.values())

    def _load_file(self):
        with open(self.__file_name, "r") as content:
            for lines in content:
                # line=lines
                # first_comma=line.find(",")
                # id=lines[:first_comma]
                # line=line[first_comma+1:]
                # second_comma=line.find(",")
                # name=line[:second_comma]
                # solution=line[second_comma+1:]
                argument=lines.split(",")
                assignment = Assignment(int(argument[0]),argument[1],argument[2])
                self.add_assignment(assignment)

    def save_file(self):
        with open(self.__file_name,"w") as f:
            for assignment in self.return_assignments():
                f.write(f"{assignment.id},{assignment.student_name},{assignment.solution}")




# homeworks=HomeworksFile("input.txt")
# print(homeworks.return_assignments())
# homeworks.add_assignment(Assignment(4,"Bot","Done"))
# print(homeworks.return_assignments())
