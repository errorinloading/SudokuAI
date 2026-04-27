import random

base = 3
side = base * base


def pattern(r, c):
    return (base * (r % base) + r // base + c) % side


def shuffle(s):
    return random.sample(s, len(s))


def generate_board():

    r_base = range(base)

    rows = [g * base + r for g in shuffle(r_base) for r in shuffle(r_base)]
    cols = [g * base + c for g in shuffle(r_base) for c in shuffle(r_base)]

    nums = shuffle(range(1, side + 1))

    board = [
        [nums[pattern(r, c)] for c in cols]
        for r in rows
    ]

    # REMOVE CELLS
    squares = side * side
    empty = 45

    for p in random.sample(range(squares), empty):

        board[p // side][p % side] = 0

    return board