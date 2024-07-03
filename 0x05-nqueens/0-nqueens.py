#!/usr/bin/python3

from sys import argv


def backtrack(r):
    if r == n:
        copy = ["".join(row) for row in board]
        res.append(copy)
        return
    for c in range(n):
        if c in col or (r + c) in posDiag or (r - c) in negDiag:
            continue
        col.add(c)
        posDiag.add(r + c)
        negDiag.add(r - c)
        board[r][c] = "Q"
        backtrack(r + 1)
        col.remove(c)
        posDiag.remove(r + c)
        negDiag.remove(r - c)
        board[r][c] = "."


if len(argv) != 2:
    print('Usage: nqueens N')
    exit(1)
try:
    n = int(argv[1])
except BaseException:
    print('N must be a number')
    exit(1)
if n < 4:
    print('N must be at least 4')
    exit(1)
else:
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)

    res = []
    board = [["."] * n for i in range(n)]
    backtrack(0)
    final = []

    # print(res)

    for i in range(0, len(res)):
        # print(res[i])
        gg = []
        for j in range(0, len(res[i])):
            # print(res[i][j])
            for k in range(0, len(res[i][j])):
                if res[i][j][k] == "Q":
                    # print("HIIIIIIII")
                    # print(j, k)
                    gg.append([j, k])
        final.append(gg)

    for pr in final:
        print(pr)
