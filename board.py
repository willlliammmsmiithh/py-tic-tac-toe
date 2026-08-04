def create_board(): return [' '] * 9
def mark(board, idx, char): board[idx] = char
def display(board):
    for i in range(0, 9, 3):
        print('|'.join(board[i:i+3]))