# Write your solution here
def play_turn(game_board: list, x: int, y: int, piece: str):
    
    if ((x < 0) or (x > 2) or (y < 0) or (y > 2)):
        return False
    if game_board[y][x] == "":
        game_board[y][x] = piece
        return True
    return False

if __name__ == "__main__":
    print(play_turn([['', 'X', 'X'], ['', '', 'O'], ['X', 'O', '']], 2, -1, "X"))