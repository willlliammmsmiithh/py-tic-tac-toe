import board
if __name__ == '__main__':
    b = board.create_board()
    board.mark(b, 0, 'X')
    board.display(b)