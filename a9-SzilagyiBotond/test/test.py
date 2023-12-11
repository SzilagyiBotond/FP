from repository.board import Board
import unittest


class TestBoard(unittest.TestCase):
    def runTest(self):
        self.board=Board()
        self.board.save_move(0,0,'C')
        self.assertEqual(self.board.board[0][0],'C')
        self.board.delete_move(0,0)
        self.assertEqual(self.board.board[0][0],0)
        self.board.save_move(4,5,'H')
        self.board.clear_board()
        self.assertEqual(self.board.board[4][5],0)