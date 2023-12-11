from services.game_moves import ComputerMoves, HumanMoves
from services.service_exceptions import ServiceExceptions
from repository.board import Board

class GameConsole:
    def __init__(self, human: HumanMoves, computer: ComputerMoves):
        self.human = human
        self.computer = computer

    def print_board(self):
        print(self.computer.board_status())

    def print_instructions(self):
        print("Hello there traveler! Sit and play an easy game of obstruction")
        print("The rules are simple: be the last one, that makes a move")
        print("You shall start, but keep in mind, that the board is 7*6 big")
        print("(Do not fear, the computer is dumber than you think)")

    def human_moves(self):
        row = int(input("In what row shall I place you a mark: "))
        column = int(input("In what column should be the mark: "))
        self.human.human_move(row-1, column-1)

    def analyze_if_the_game_is_over(self):
        if self.computer.scan_for_end():
            return True
        return False

    def announce_winner(self, winner):
        if winner == "Human":
            print("Congratulation, you won the game")
        else:
            print("How unfortunate, you lost the game")

    def ask_for_rematch(self):
        command = int(input("If you want to rematch, press 1, if not, press anything you want(you fear to play):"))
        return command

    def clear_board(self):
        self.computer.clear_board()

    def run_game(self):
        while True:
            try:
                self.human_moves()
                if self.analyze_if_the_game_is_over():
                    self.announce_winner("Human")
                    return
                self.print_board()
                self.computer.computer_move()
                if self.analyze_if_the_game_is_over():
                    self.announce_winner("Computer")
                    return
                self.print_board()
            except ServiceExceptions as se:
                print(se)

    def run_console(self):
        self.print_instructions()
        while True:
            self.clear_board()
            self.print_board()
            self.run_game()
            if self.ask_for_rematch()!=1:
                break

board=Board()
human=HumanMoves(board)
computer=ComputerMoves(board)
console=GameConsole(human,computer)
console.run_console()