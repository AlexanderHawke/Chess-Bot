class ChessBot:

    def __init__(self):
        self.board = [[0]*8]*8
        self.whitePieces = {
                            "pawns":    [(0,1), (1,1), (2,1), (3,1), (4,1), (5,1), (6,1), (7,1)], 
                            "knights":  [(1,0), (6,0)], 
                            "bishops":  [(2,0), (5,0)], 
                            "rooks":    [(0,0), (7,0)], 
                            "queens":   [(3,0)], 
                            "king":     [(4,0)]
                            }

        self.blackPieces = {
                            "pawns":    [(0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (6,6), (7,6)], 
                            "knights":  [(1,7), (6,7)], 
                            "bishops":  [(2,7), (5,7)], 
                            "rooks":    [(0,7), (7,7)], 
                            "queens":   [(3,7)], 
                            "king":     [(4,7)]
                            }

        self.playerWhite = True
        self.materialCost = {"pawns": 1, "knights": 3, "bishops": 3, "rooks": 5, "queens": 8, "king": 1000}

    def __str__(self):
        return  '\n'.join(' '.join(str(x) for x in row) for row in self.board)

    def __repr__(self):
        return str(self.board) + "LOL!"

    def setupBoard(self):
        # INFO: print(self.whitePieces["pawns"]) 
        # INFO: [(1, 2), (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)]

        for key, value in self.whitePieces.items():
            for piece in value:
                print("WhitePieces: ")
                print(piece)
                print(piece[0], piece[1])
                self.board[piece[0]][piece[1]] = key
        for key, value in self.blackPieces.items():
            for piece in value:
                print("BlackPieces: ")
                print(piece)
                print(piece[0], piece[1])
                self.board[piece[0]][piece[1]] = key

chessBot = ChessBot()
chessBot.setupBoard()
print(chessBot)
repr(chessBot)