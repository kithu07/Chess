CHESS_BOARD = [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'],
               ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'],
               ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'],
               ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'],
               ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'],
               ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'],
               ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'],
               ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']]

def current_index(current_pos : str) -> int:
    for i in range(len(CHESS_BOARD)):
        for j in range(len(CHESS_BOARD)):
            if CHESS_BOARD[i][j] == current_pos:
                return i ,j

def positions_list(ranks :int , files : int) -> list[str]:
    rows = r = i = ranks
    columns = c = j = files
    pos_list=[]

    while ranks <= len(CHESS_BOARD)-1 and files <= len(CHESS_BOARD)-1 :
        pos_list.append(CHESS_BOARD[ranks][files])
        ranks+= 1
        files+= 1
    while rows >= 0 and columns >= 0:
        pos_list.append(CHESS_BOARD[rows][columns])
        rows-= 1
        columns-= 1
    while r <= len(CHESS_BOARD)-1 and c >= 0:
        pos_list.append(CHESS_BOARD[r][c])
        r+= 1
        c-= 1
    while i >= 0 and j <= len(CHESS_BOARD)-1:
        pos_list.append(CHESS_BOARD[i][j])
        i-= 1
        j+= 1
    return list(set(pos_list))

def bishop_movements(current_pos : str) -> list[str]:
    ranks , files = current_index(current_pos)
    return positions_list(ranks ,files)
