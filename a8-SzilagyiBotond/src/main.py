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
from src.ui.ui import Console

stud_repo = StudentRepository(StudentValidator())
stud_service = StudentServices(stud_repo)
disc_repo = DisciplineRepository(DisciplineValidator())
disc_services = DisciplineServices(disc_repo)
grade_repo = GradeRepository(GradeValidator())
grade_services = GradeServices(grade_repo, stud_repo, disc_repo)
console = Console(grade_services, stud_service, disc_services)
console.run_console()
