# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
    count = 0
    for line in my_matrix:
        i = 0
        while (i < len(line)):
            if line[i] == element:
                count += 1
            i+=1
    return count

def who_won(game_board: list):
    player1 = count_matching_elements(game_board, 1)
    player2 = count_matching_elements(game_board, 2)
    if player1 > player2:
        return 1
    elif player2 > player1:
        return 2
    else:
        return 0
    
