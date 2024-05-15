def can_cut(piece1: str, pos1: str, piece2: str, pos2: str) -> str:
    pieces = ["rook", "knight", "queen", "bishop"]
    piece1_fname = [rook_movements(pos1), knight_movements(pos1), queen_movements(pos1), bishop_movements(pos1)]
    piece2_fname = [rook_movements(pos2), knight_movements(pos2), queen_movements(pos2), bishop_movements(pos2)]
    for i in range(len(pieces)):
        if piece1 == pieces[i]:
            piece1_movements = piece1_fname[i]
        if piece2 == pieces[i]:
            piece2_movements = piece2_fname[i] 
    if pos1 in piece2_movements and pos2 in piece1_movements:
        return "Both can cut each other"     
    elif pos1 in piece2_movements:
        return piece2 + " cuts " + piece1
    elif pos2 in piece1_movements:
        return piece1 + " cuts " + piece2
    else:
        return "Can't cut"