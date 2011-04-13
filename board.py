class board:
    maxX = 7
    maxY = 6

    emptySpace = 0
    playerMove = 1
    computerMove = 2
    
    def __init__(self):
        self.spaces = [[board.emptySpace for i in range(board.maxY)] for j in range(board.maxX)]

    def setSpace(self, x, y, val):
        if x >= board.maxX or y >= board.maxY:
            raise IndexError
            
        if type(val) is not int:
            raise TypeError
        
        if val != board.emptySpace and val != board.playerMove and val != board.computerMove:
            raise ValueError
        
        self.spaces[y][x] = val
        
    def getSpace(self, x, y):
        if x >= board.maxX or y >= board.maxY:
            raise IndexError
        return self.spaces[y][x]
    
    def __str__(self):
        #print self.spaces
        for i, row in enumerate(self.spaces):
            for j, space in enumerate(row):
                print i,j, space
        return str(self.spaces)

if __name__ == "__main__":
    myBoard = board()
    
    myBoard.setSpace(5,3,board.playerMove)
    
    str(myBoard)
    
    