class ChessGame:

    def __init__(self):
        
        # The board in the starting position with the white pieces facing the player.
        self.whiteBoardStarting = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        # The board in the starting position with the black pieces facing the player.
        self.blackBoardStarting = [
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            [" ", " ", " ", " ", " ", " ", " ", " "],
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"]
        ]
        
        self.player = input("What side would you like to play as? (white or black) ").strip().lower()
        while self.player != "black" and self.player != "white":
            self.player = input("Please input an appropriate answer, what side would you like to play as? (white or black) ")

        self.board = []
        
        if self.player == "white":
            self.board = self.whiteBoardStarting
        if self.player == "black":
            self.board = self.blackBoardStarting
        
        self.materialCost = {"wP": 1, "bP": 1, # Pawns are worth 1
                             "wN": 3, "bN": 3, # Knights are worth 3
                             "wB": 3, "bB": 3, # Bishops are worth 3
                             "wR": 5, "bR": 5, # Rooks are worth 5
                             "wQ": 9, "bQ": 9, # Queens are worth 9
                             "wK": 1000, "bK": 1000} # Kings are worth 1000
        
        # Pawn position scores (player perspective)
        # Higher values for advancing pawns, center files favored
        self.pawnScores = [
            [90, 90, 90, 90, 90, 90, 90, 90], # Rank 8 - PROMOTION! Highest value
            [50, 50, 50, 50, 50, 50, 50, 50], # Rank 7 - Almost there
            [10, 10, 20, 30, 30, 20, 10, 10], # Rank 6 - Advanced
            [5,  5, 10, 25, 25, 10,  5,  5],  # Rank 5 - Good progress
            [0,  0,  0, 20, 20,  0,  0,  0],  # Rank 4 - Center control
            [5, -5,-10,  0,  0,-10, -5,  5],  # Rank 3 - Don't rush edge pawns
            [5, 10, 10,-20,-20, 10, 10,  5],  # Rank 2 - Starting rank
            [0,  0,  0,  0,  0,  0,  0,  0]   # Rank 1 - No pawns should be here
        ]

        # Knight position scores
        # "Knights on the rim are dim" - center squares highly valued
        self.knightScores = [
            [-50,-40,-30,-30,-30,-30,-40,-50],
            [-40,-20,  0,  0,  0,  0,-20,-40],
            [-30,  0, 10, 15, 15, 10,  0,-30],
            [-30,  5, 15, 20, 20, 15,  5,-30],
            [-30,  0, 15, 20, 20, 15,  0,-30],
            [-30,  5, 10, 15, 15, 10,  5,-30],
            [-40,-20,  0,  5,  5,  0,-20,-40],
            [-50,-40,-30,-30,-30,-30,-40,-50]
        ]

        # Bishop position scores
        # Long diagonals and center control favored
        self.bishopScores = [
            [-20,-10,-10,-10,-10,-10,-10,-20],
            [-10,  0,  0,  0,  0,  0,  0,-10],
            [-10,  0,  5, 10, 10,  5,  0,-10],
            [-10,  5,  5, 10, 10,  5,  5,-10],
            [-10,  0, 10, 10, 10, 10,  0,-10],
            [-10, 10, 10, 10, 10, 10, 10,-10],
            [-10,  5,  0,  0,  0,  0,  5,-10],
            [-20,-10,-10,-10,-10,-10,-10,-20]
        ]

        # Rook position scores
        # Open files and 7th rank favored
        self.rookScores = [
            [0,  0,  0,  0,  0,  0,  0,  0],
            [5, 10, 10, 10, 10, 10, 10,  5],
            [-5,  0,  0,  0,  0,  0,  0, -5],
            [-5,  0,  0,  0,  0,  0,  0, -5],
            [-5,  0,  0,  0,  0,  0,  0, -5],
            [-5,  0,  0,  0,  0,  0,  0, -5],
            [-5,  0,  0,  0,  0,  0,  0, -5],
            [0,  0,  0,  5,  5,  0,  0,  0]
        ]

        # Queen position scores
        # Modest center preference, avoid early development
        self.queenScores = [
            [-20,-10,-10, -5, -5,-10,-10,-20],
            [-10,  0,  0,  0,  0,  0,  0,-10],
            [-10,  0,  5,  5,  5,  5,  0,-10],
            [ -5,  0,  5,  5,  5,  5,  0, -5],
            [  0,  0,  5,  5,  5,  5,  0, -5],
            [-10,  5,  5,  5,  5,  5,  0,-10],
            [-10,  0,  5,  0,  0,  0,  0,-10],
            [-20,-10,-10, -5, -5,-10,-10,-20]
        ]

        # King position scores
        # Castled positions favored, center is dangerous
        self.kingScores = [
            [-30,-40,-40,-50,-50,-40,-40,-30],
            [-30,-40,-40,-50,-50,-40,-40,-30],
            [-30,-40,-40,-50,-50,-40,-40,-30],
            [-30,-40,-40,-50,-50,-40,-40,-30],
            [-20,-30,-30,-40,-40,-30,-30,-20],
            [-10,-20,-20,-20,-20,-20,-20,-10],
            [ 20, 20,  0,  0,  0,  0, 20, 20],
            [ 20, 30, 10,  0,  0, 10, 30, 20]
        ]

        

    def __str__(self):
        return  '\n'.join(' '.join(str(x) for x in row) for row in self.board)
    
    

chessGame = ChessGame()
print(chessGame)