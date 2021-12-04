"""
Advent of Code
2021 Day 4

@author: Tom Herbert
"""

def open_file():
    file = open("Day" + str(day) + "inputs.txt")
    inputs = file.read().split("\n\n")
    file.close()
    return inputs

def format_data():
    global called, boards, marked
    called = [int(val) for val in inputs.pop(0).split(",")]
    boards = [[int(val) for val in board.split()] for board in inputs]
    marked = [[0 for i in range(len(board))] for board in boards]
    
def mark_board(calledNo):
    for i, board in enumerate(boards):
        if calledNo in board:
            idx = board.index(calledNo)
            marked[i][idx] = 1

def check_bingo():
    boardSize = 5
    for i, board in enumerate(marked):
        bingo = False
        for j in range(boardSize):
            row = sum(board[j*boardSize:(j+1)*boardSize])
            col = sum(board[j::5])
            if row == boardSize or col == boardSize:
                bingo = True
                break
        if bingo:
            return bingo, i
    return bingo, -1

def calculate_score(boardNo, calledNo):
    unmarked = 0
    for i, val in enumerate(marked[boardNo]):
        if val == 0:
            unmarked += boards[boardNo][i]
    score = unmarked * calledNo
    return score

def part_one():
    for num in called:
        mark_board(num)
        bingo, board = check_bingo()
        if bingo:
            score = calculate_score(board, num)
            break
    print(f"Part One = {score}")

def part_two():
    global marked
    marked = [[0 for i in range(len(board))] for board in boards]
    for num in called:
        mark_board(num)
        bingo = True
        while bingo and len(boards) > 1:
            bingo, board = check_bingo()
            if bingo:
                boards.pop(board)
                marked.pop(board)
        bingo, board = check_bingo()
        if bingo:
            score = calculate_score(board, num)
            break
    print(f"Part Two = {score}")

day = 4
inputs = open_file()

format_data()

part_one()
part_two()