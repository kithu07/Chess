def queen_movements(current_pos : str) ->list:
    return list(set(rook_movements(current_pos) + bishop_movements(current_pos)))

