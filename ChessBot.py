class ChessBot:

    def __init__(self):
        
        # Initialize the board as the starting position with the white pieces facing the player.
        self.board = [
        ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
        ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
        ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        self.playerWhite = True
        self.materialCost = {"wP": 1, "bP": 1, # Pawns are worth 1
                             "wN": 3, "bN": 3, # Knights are worth 3
                             "wB": 3, "bB": 3, # Bishops are worth 3
                             "wR": 5, "bR": 5, # Rooks are worth 5
                             "wQ": 9, "wQ": 9, # Queens are worth 9
                             "wK": 1000, "bK": 1000} # Kings are worth 1000

    def __str__(self):
        return  '\n'.join(' '.join(str(x) for x in row) for row in self.board)

    def __repr__(self):
        return str(self.board) + "LOL!"

chessBot = ChessBot()
print(chessBot)
repr(chessBot)