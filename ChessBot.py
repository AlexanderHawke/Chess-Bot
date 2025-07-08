class ChessGame:

    def __init__(self):
        
        # White pieces defined and their score values
        self.whitePieces = {"wP": 1,
                            "wN": 3,
                            "wB": 3,
                            "wR": 5,
                            "wQ": 9,
                            "wK": 1000}
        
        # Black pieces defined and their score values
        self.blackPieces = {"bP": 1,
                            "bN": 3,
                            "bB": 3,
                            "bR": 5,
                            "bQ": 9,
                            "bK": 1000}

        # The board in the starting position with the white pieces facing the player.
        self.whiteBoardStarting = [
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
        ]

        # The board in the starting position with the black pieces facing the player.
        self.blackBoardStarting = [
            ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
            ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
            ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
            ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"]
        ]

        # Ask the player what colour pieces they would like to play
        self.player = input("What side would you like to play as? ('white' or 'black') ").strip().lower()
        while self.player != "black" and self.player != "white":
            self.player = input("Please input an appropriate answer, what side would you like to play as? ('white' or 'black') ")
        
        # set the board so that the player's pieces are on the bottom always, and assign player/computer Pieces
        if self.player == "white":
            self.board = self.whiteBoardStarting
            self.playerPieces = self.whitePieces
            self.computerPieces = self.blackPieces
        else:
            self.board = self.blackBoardStarting
            self.playerPieces = self.blackPieces
            self.computerPieces = self.whitePieces
        
        # Pawn position scores (PLAYER perspective)
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

        # relates a piece to their respective score table for easy lookup of piece value (piece value * positional scoring)
        self.scoreTables = {
            "P": self.pawnScores,
            "N": self.knightScores,
            "B": self.bishopScores,
            "R": self.rookScores,
            "Q": self.queenScores,
            "K": self.kingScores
        }

    # Prints the game board as a string
    def __str__(self):
        return  '\n'.join(' '.join(str(x) for x in row) for row in self.board)

    # Evaluates the game state of the board (player favoured is positive, computer favoured is negative)
    def evaluate(self):
        playerScore = 0
        computerScore = 0
        for i in range(8):
            for j in range(8):
                if self.board[i][j] in self.playerPieces:
                    playerScore += self.playerPieces[self.board[i][j]] * (1/self.scoreTables[self.board[i][j][1]][i][j])
                if self.board[i][j] in self.computerPieces:
                    computerScore += self.computerPieces[self.board[i][j]] * (1/self.scoreTables[self.board[i][j][1]][7-i][7-j])
        
        return playerScore - computerScore

chessGame = ChessGame()
chessGame.board = [
                    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
                    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
                    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                    ["  ", "  ", "  ", "  ", "  ", "  ", "  ", "  "],
                    ["  ", "  ", "  ", "  ", "wP", "  ", "  ", "  "],
                    ["wP", "wP", "wP", "wP", "  ", "wP", "wP", "wP"],
                    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"]
                ]

print(chessGame)
print("Evaluation: ", chessGame.evaluate())