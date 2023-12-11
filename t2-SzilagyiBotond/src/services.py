from src.domain import Assignment
from src.repository import HomeworksFile


class AssignmentServices:
    def __init__(self, homework_assignments: HomeworksFile):
        self.__homework = homework_assignments

    def add_assignment(self, id, name, solution):
        assignment = Assignment(id, name, solution)
        self.__homework.add_assignment(assignment)
        self.__homework.save_file()

    def list_all_assignments(self):
        return self.__homework.return_assignments()

    def dishonesty_check(self):
        dishonest_assignment_pairs=[]
        for assignment in self.list_all_assignments():
            for assignment_to_compare in self.list_all_assignments():
                solution_1=assignment.solution
                solution_1=solution_1.split(" ")
                solution_2=assignment_to_compare.solution
                solution_2=solution_2.split(" ")
                tally=0
                for word in solution_1:
                    for word_2 in solution_2:
                        if word==word_2 and assignment!=assignment_to_compare:
                            tally +=1
                if tally/len(solution_1)>0.2:
                    dishonest_pair=[assignment.student_name,assignment_to_compare.student_name, "The common part: ", tally/len(solution_1)]
                    dishonest_assignment_pairs.append(dishonest_pair)
        return dishonest_assignment_pairs