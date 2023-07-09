
class ChessBoard:
    def __init__(self) -> None:
        self.board = [[Unit(i,j) for j in range(8)] for i in range(8)]
        for i in range(8):
            self.board[1][i] = Pawn(1, i)
            self.board[6][i] = Pawn(6, i)

    def __str__(self) -> str:
        for i in range(8):
            line = " ".join([str(self.board[i][j]) for j in range(8)])
            print(line)
    
class Unit:
    name = "U"
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y

    def move(self, x, y):
        '''
        将一个点移动到另一个点，并且检查移动的合法性
        '''
        pass 

    def __str__(self) -> str:
        return self.name


class Pawn(Unit):
    name = "P"
    def __init__(self, x, y) -> None:
        super().__init__(x, y)
    
    # def __str__(self):
    #     return f"pawn at ({self.x}, {self.y})"

class Queen(Unit):
    def __init__(self, x, y) -> None:
        super().__init__(x, y)


chessboard = ChessBoard()
#print(chessboard.board[1][3])
print(chessboard)