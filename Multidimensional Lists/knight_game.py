# Chess is the oldest game, but it is still popular these days. 
# You will use only one chess piece for this task - the Knight.
# A chess knight has 8 possible moves it can make.
# It can move to the nearest square but not on the same row, column, or diagonal. 
# (e.g., it can move two squares horizontally, then one square vertically, 
# or it can move one square horizontally then two squares vertically - i.e., in an "L" pattern.) 
# The knight game is played on a board with dimensions N x N.
# You will receive a board with a "K" for knights and a "0" for empty cells. 
# Your task is to remove knights until no knights that can attack one another with one move are left. 
# Always remove the knight who can attack the greatest number of knights. 
# If there are two or more knights with the same number of attacks, remove the top-left one.

n = int(input())

chess_board = []

for _ in range(n):
    data = [x for x in input()]
    chess_board.append(data)

possible_moves = [(-2, +1), (-2, -1),
                  (-1, +2), (+1, +2),
                  (-1, -2), (+1, -2),
                  (+2, -1), (+2, +1)
                  ]

removed = 0

while True:
    max_attacks = 0
    remove_r, remove_c = -1 , -1

    for rol in range(n):
        for col in range(n):
            attacks = 0
            if chess_board[rol][col] == "K":
                for possible_row, possible_col in possible_moves:
                    amr = rol + possible_row
                    amc = col + possible_col
                    if 0 <= amr < n and 0 <= amc < n and chess_board[amr][amc] == "K":
                        attacks += 1
                if attacks > max_attacks:
                    max_attacks = attacks
                    remove_r, remove_c = rol, col

    if max_attacks == 0:
        break

    chess_board[remove_r][remove_c] = "0"
    removed += 1

print(removed)
