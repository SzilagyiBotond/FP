from dataclasses import dataclass


@dataclass
class StudentAverageDTO:
    student_id: str
    discipline_id: str
    average_grade_value: float

    def __str__(self):
        return str(self.student_id) + str(self.discipline_id) + str(self.average_grade_value) + '\n'


@dataclass
class DisciplineAverageDTO:
    discipline_id: str
    average: float


@dataclass
class StudentGeneralAverageDTO:
    student_id: str
    average_all: float

    def __str__(self):
        return str(self.student_id) + str(self.average_all) + '\n'
