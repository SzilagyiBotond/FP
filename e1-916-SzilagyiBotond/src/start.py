from ui.ui import *
from service.actions import *
from domain.question import *
from repository.MasterQuestions import *


validator=QuestionValidator()
master=MasterQuestions(validator,"master.txt")
master.generate_100_random_entries()
action=GameActions(master)
ui=Ui(action)
ui.run_console()
