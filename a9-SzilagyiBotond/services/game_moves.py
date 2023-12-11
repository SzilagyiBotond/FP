from repository.board import Board
from services.service_exceptions import ServiceExceptions


class ComputerMoves:
    def __init__(self, board):
        self.board = board

    def board_status(self):
        return self.board

    def scan_for_end(self):
        for row in range(self.board.rows):
            for column in range(self.board.columns):
                if self.board.board[row][column] == 0:
                    return False
        return True

    def search_move_that_wins_game(self):
        for row in range(self.board.rows):
            for column in range(self.board.columns):
                if self.board.board[row][column] == 0:
                    self.board.save_move(row, column, "C")
                    if self.scan_for_end() is True:
                        self.board.delete_move(row, column)
                        return row, column
                    self.board.delete_move(row,column)
        return None
    def clear_board(self):
        self.board.clear_board()

    def search_moves_that_lose_game(self):
        is_lost = False
        row1, column1 = self.search_moves_that_covers_most_squares()
        self.board.save_move(row1, column1, 'C')
        if self.scan_for_end():
            self.board.delete_move(row1, column1)
            return False
        row2, column2 = self.search_moves_that_covers_most_squares()
        self.board.save_move(row2, column2, 'C')
        if self.scan_for_end():
            is_lost = True
        self.board.delete_move(row1, column1)
        self.board.delete_move(row2, column2)
        return is_lost

    def search_moves_that_covers_most_squares(self):
        most_open_squares = 0
        move_row = 0
        move_column = 0
        for row in range(self.board.rows):
            for column in range(self.board.columns):
                if self.board.board[row][column] == 0:
                    open_squares = 0
                    if row != 0 and row != self.board.rows - 1:
                        if column == 0:
                            for i in range(0, 3):
                                if self.board.board[row + i - 1][column] == 0:
                                    open_squares += 1
                                if self.board.board[row + i - 1][column + 1] == 0:
                                    open_squares += 1
                        if column == (self.board.columns - 1):
                            for i in range(0, 3):
                                if self.board.board[row + i - 1][column] == 0:
                                    open_squares += 1
                                if self.board.board[row + i - 1][column - 1] == 0:
                                    open_squares += 1
                        if column != 0 and column != (self.board.columns - 1):
                            for i in range(0, 3):
                                if self.board.board[row + i - 1][column] == 0:
                                    open_squares += 1
                                if self.board.board[row + i - 1][column - 1] == 0:
                                    open_squares += 1
                                if self.board.board[row + i - 1][column + 1] == 0:
                                    open_squares += 1
                    if row == 0:
                        if column == 0:
                            for i in range(0, 2):
                                if self.board.board[row + i][column] == 0:
                                    open_squares += 1
                                if self.board.board[row + i][column + 1] == 0:
                                    open_squares += 1
                        if column == (self.board.columns - 1):
                            for i in range(0, 2):
                                if self.board.board[row + i][column] == 0:
                                    open_squares += 1
                                if self.board.board[row + i][column - 1] == 0:
                                    open_squares += 1
                        if column != 0 and column != (self.board.columns - 1):
                            for i in range(0, 2):
                                if self.board.board[row + i][column] == 0:
                                    open_squares += 1
                                if self.board.board[row + i][column - 1] == 0:
                                    open_squares += 1
                                if self.board.board[row + i][column + 1] == 0:
                                    open_squares += 1
                    if row == (self.board.rows - 1):
                        if column == 0:
                            for i in range(0, 2):
                                if self.board.board[row - i][column] == 0:
                                    open_squares += 1
                                if self.board.board[row - i][column + 1] == 0:
                                    open_squares += 1
                        if column == (self.board.columns - 1):
                            for i in range(0, 2):
                                if self.board.board[row - i][column] == 0:
                                    open_squares += 1
                                if self.board.board[row - i][column - 1] == 0:
                                    open_squares += 1
                        if column != 0 and column != (self.board.columns - 1):
                            for i in range(0, 2):
                                if self.board.board[row - i][column] == 0:
                                    open_squares += 1
                                if self.board.board[row - i][column - 1] == 0:
                                    open_squares += 1
                                if self.board.board[row - i][column + 1] == 0:
                                    open_squares += 1
                    if open_squares > most_open_squares:
                        most_open_squares = open_squares
                        move_row = row
                        move_column = column
        return move_row, move_column

    def computer_move(self):
        # if self.search_move_that_wins_game() is not None:
        #     row,column=self.search_move_that_wins_game()
        #     self.board.save_move(row,column,'C')
        # if self.search_move_that_wins_game() is None:
        row, column = self.search_moves_that_covers_most_squares()
        self.board.save_move(row, column, 'C')
        # else:
        #     row, column = self.search_move_that_wins_game()
        #     self.board.save_move(row,column,'C')


class HumanMoves:
    def __init__(self, board):
        self.board = board

    def human_move(self, row, column):
        if 0 > row + 1 or self.board.rows < row + 1 or self.board.columns < column + 1 or 0 > column + 1:
            raise ServiceExceptions("Invalid move, you are out of bounds")
        if self.board.board[row][column] != 0:
            raise ServiceExceptions("Field already occupied, invalid move")
        self.board.save_move(row, column, 'H')
