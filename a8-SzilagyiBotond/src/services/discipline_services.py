from src.repository.discipline_repository import DisciplineRepository
from src.domain.entities import Discipline
from src.domain.validators import DisciplineValidator
from src.services.grade_services import GradeServices
from src.services.service_exceptions import ServiceExceptions


class DisciplineServices:
    def __init__(self, discipline_repository:DisciplineRepository):
        self.__discipline_repository = discipline_repository

    def add_discipline(self, discipline_id, discipline_name):
        discipline = Discipline(discipline_id, discipline_name)
        self.__discipline_repository.add(discipline)

    def delete_discipline(self, discipline_id):
        discipline = self.__discipline_repository.find_by_id(discipline_id)
        if discipline is None:
            raise ServiceExceptions("There is no such discipline")
        self.__discipline_repository.delete(discipline)

    def list_all_discipline(self):
        # for discipline in self.__discipline_repository.find_all_disciplines():
        #     print(discipline)
        return self.__discipline_repository.find_all_disciplines()

    def update_discipline(self, discipline_id, new_discipline_name):
        discipline = Discipline(discipline_id, new_discipline_name)
        if self.__discipline_repository.find_by_id(discipline_id) is None:
            raise ServiceExceptions("There is no such discipline")
        self.__discipline_repository.update(discipline)

    def find_discipline_by_name(self, discipline_name):
        # for discipline in self.__discipline_repository.find_by_name(discipline_name):
        #     print( discipline)
        return self.__discipline_repository.find_by_name(discipline_name)

    def find_discipline_by_id(self,discipline_id):
        if self.__discipline_repository.find_by_id(discipline_id) is None:
            raise ServiceExceptions("Discipline doesnt exist")
        # print(self.__discipline_repository.find_by_id(discipline_id))
        return self.__discipline_repository.find_by_id(discipline_id)


discipline_validator = DisciplineValidator()
discipline_repository = DisciplineRepository(discipline_validator)
discipline_service = DisciplineServices(discipline_repository)

