CHESS_BOARD = [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
               ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
               ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
               ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
               ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
               ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
               ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
               ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']]

def current_place(pos : str) -> tuple:
    ranks, files = 0, 0
    for rank in CHESS_BOARD:
        if pos in rank:
            ranks = CHESS_BOARD.index(rank)
            files = CHESS_BOARD[ranks].index(pos)
            return (ranks, files)     

def is_valid(square : tuple) -> bool:
    return square[0] in range(8) and square[1] in range(8)
    

def knight_movements(pos : str):
    (rank, file) = current_place(pos)
    step = [-2, 2,-1, 1]
    moves = []
    for r in step:
        for f in step:
            #print(CHESS_BOARD[rank + r] [file + f])
            if abs(f) != abs(r) and is_valid((rank + r, file + f)):        
                moves.append(CHESS_BOARD[rank + r] [file + f])
    return moves
