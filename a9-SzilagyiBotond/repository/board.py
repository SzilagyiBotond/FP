from repository.repository_exceptions import RepositoryExceptions


class Board:
    def __init__(self, rows=7, columns=6):
        self.rows = rows
        self.columns = columns
        self.board = [[0] * self.columns for _ in range(rows)]


    def clear_board(self):
        self.board = [[0] * 6 for _ in range(7)]

    def delete_move(self, row, column):
        if row != 0 and row != self.rows - 1:
            if column == 0:
                self.board[row - 1][column] = 0
                self.board[row - 1][column + 1] = 0
                self.board[row + 1][column] = 0
                self.board[row + 1][column + 1] = 0
                self.board[row][column + 1] = 0
                self.board[row][column] = 0
            if column == (self.columns - 1):
                self.board[row - 1][column] = 0
                self.board[row - 1][column - 1] = 0
                self.board[row + 1][column] = 0
                self.board[row + 1][column - 1] = 0
                self.board[row][column - 1] = 0
                self.board[row][column] = 0
            if column != 0 and column != (self.columns - 1):
                for i in range(0, 3):
                    self.board[row - 1 + i][column - 1] = 0
                    self.board[row - 1 + i][column] = 0
                    self.board[row - 1 + i][column + 1] = 0

        if row == 0:
            if column == 0:
                self.board[row + 1][column] = 0
                self.board[row + 1][column + 1] = 0
                self.board[row][column + 1] = 0
                self.board[row][column] = 0
            if column == (self.columns - 1):
                self.board[row + 1][column] = 0
                self.board[row + 1][column - 1] = 0
                self.board[row][column - 1] = 0
                self.board[row][column] = 0
            if column != 0 and column != (self.columns - 1):
                for i in range(0, 2):
                    self.board[row + i][column - 1] = 0
                    self.board[row + i][column] = 0
                    self.board[row + i][column + 1] = 0

        if row == (self.rows - 1):
            if column == 0:
                self.board[row - 1][column] = 0
                self.board[row - 1][column + 1] = 0
                self.board[row][column + 1] = 0
                self.board[row][column] = 0
            if column == (self.columns - 1):
                self.board[row - 1][column] = 0
                self.board[row - 1][column - 1] = 0
                self.board[row][column - 1] = 0
                self.board[row][column] = 0
            if column != 0 and column != (self.columns - 1):
                for i in range(0, 2):
                    self.board[row - i][column - 1] = 0
                    self.board[row - i][column] = 0
                    self.board[row - i][column + 1] = 0


    def save_move(self, row, column, mark):
        if row != 0 and row != self.rows - 1:
            if column == 0:
                self.board[row - 1][column] = 'x'
                self.board[row - 1][column + 1] = 'x'
                self.board[row + 1][column] = 'x'
                self.board[row + 1][column + 1] = 'x'
                self.board[row][column + 1] = 'x'
                self.board[row][column] = mark
            if column == (self.columns - 1):
                self.board[row - 1][column] = 'x'
                self.board[row - 1][column - 1] = 'x'
                self.board[row + 1][column] = 'x'
                self.board[row + 1][column - 1] = 'x'
                self.board[row][column - 1] = 'x'
                self.board[row][column] = mark
            if column != 0 and column != (self.columns - 1):
                for i in range(0, 3):
                    self.board[row - 1 + i][column - 1] = 'x'
                    self.board[row - 1 + i][column] = 'x'
                    self.board[row - 1 + i][column + 1] = 'x'
                self.board[row][column] = mark
        if row == 0:
            if column == 0:
                self.board[row + 1][column] = 'x'
                self.board[row + 1][column + 1] = 'x'
                self.board[row][column + 1] = 'x'
                self.board[row][column] = mark
            if column == (self.columns - 1):
                self.board[row + 1][column] = 'x'
                self.board[row + 1][column - 1] = 'x'
                self.board[row][column - 1] = 'x'
                self.board[row][column] = mark
            if column != 0 and column != (self.columns - 1):
                for i in range(0, 2):
                    self.board[row + i][column - 1] = 'x'
                    self.board[row + i][column] = 'x'
                    self.board[row + i][column + 1] = 'x'
                self.board[row][column] = mark
        if row == (self.rows - 1):
            if column == 0:
                self.board[row - 1][column] = 'x'
                self.board[row - 1][column + 1] = 'x'
                self.board[row][column + 1] = 'x'
                self.board[row][column] = mark
            if column == (self.columns - 1):
                self.board[row - 1][column] = 'x'
                self.board[row - 1][column - 1] = 'x'
                self.board[row][column - 1] = 'x'
                self.board[row][column] = mark
            if column != 0 and column != (self.columns - 1):
                for i in range(0, 2):
                    self.board[row - i][column - 1] = 'x'
                    self.board[row - i][column] = 'x'
                    self.board[row - i][column + 1] = 'x'
                self.board[row][column] = mark

    def __str__(self):
        s = ''
        for row in range(self.rows):
            for column in range(self.columns):
                s += '|' + str(self.board[row][column])
            s += '|' + '\n'
            # s += '|' + '|'.join(str(cell) for cell in row) + '|\n'
        return s

# board = Board()
#
# board.save_move(0,0 , 'H')
# print(board)
# board.delete_move(0,0)
# print(board)
