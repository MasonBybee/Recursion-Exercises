import copy

"""Boggle word check.

Given a 5x5 boggle board, see if you can find a given word in it.

In Boggle, you can start with any letter, then move in any NEWS direction.
You can continue to change directions, but you cannot use the exact same
tile twice.

So, for example::

    N C A N E
    O U I O P
    Z Q Z O N
    F A D P L
    E D E A Z

In this grid, you could find `NOON* (start at the `N` in the top
row, head south, and turn east in the third row). You cannot find
the word `CANON` --- while you can find `CANO` by starting at the
top-left `C`, you can 't re-use the exact same `N` tile on the
front row, and there's no other `N` you can reach.

For example::

    >>> board = make_board('''
    ... N C A N E
    ... O U I O P
    ... Z Q Z O N
    ... F A D P L
    ... E D E A Z
    ... ''')

`NOON` should be found (0, 3) -> (1, 3) -> (2, 3) -> (2, 4)::

    >>> find(board, "NOON")
    True

`NOPE` should be found (0, 3) -> (1, 3) -> (1, 4) -> (0, 4)::

    >>> find(board, "NOPE")
    True

`CANON` can't be found (`CANO` starts at (0, 1) but can't find
the last `N` and can't re-use the N)::

    >>> find(board, "CANON")
    False

You cannot travel diagonally in one move, which would be required
to find `QUINE`::

    >>> find(board, "QUINE")
    False

We can recover if we start going down a false path (start 3, 0)::

    >>> find(board, "FADED")
    True


An extra tricky case --- it needs to find the `N` toward the top right,
and then go down, left, up, up, right to find all four `O`s and the `S`::

    >>> board2 = make_board('''
    ... E D O S Z
    ... N S O N R
    ... O U O O P
    ... Z Q Z O R
    ... F A D P L
    ... ''')

    >>> find(board2, "NOOOOS")
    True

"""


def make_board(board_string):
    """Make a board from a string.

    For example::

        >>> board = make_board('''
        ... N C A N E
        ... O U I O P
        ... Z Q Z O N
        ... F A D P L
        ... E D E A Z
        ... ''')

        >>> len(board)
        5

        >>> board[0]
        ['N', 'C', 'A', 'N', 'E']
    """

    letters = board_string.split()

    board = [
        letters[0:5],
        letters[5:10],
        letters[10:15],
        letters[15:20],
        letters[20:25],
    ]

    return board


def find(board, word, idx=0, last_row=None, last_idx=None):
    """Can word be found in board?"""
    if idx == len(word):
        return True

    if last_row is None and last_idx is None:
        for rowIdx, row in enumerate(board):
            for numIdx, num in enumerate(row):
                if word[0] == num:
                    board[rowIdx][numIdx] = None
                    if find(board, word, idx + 1, rowIdx, numIdx):
                        board[rowIdx][numIdx] = num
                        return True
                    board[rowIdx][numIdx] = num
        return False
    else:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            new_row = last_row + direction[0]
            new_col = last_idx + direction[1]
            if (
                0 <= new_row < len(board)
                and 0 <= new_col < len(board[0])
                and board[new_row][new_col] == word[idx]
            ):
                board[new_row][new_col] = None
                if find(board, word, idx + 1, new_row, new_col):
                    board[new_row][new_col] = word[idx]
                    return True
                board[new_row][new_col] = word[idx]
        return False


if __name__ == "__main__":
    import doctest

    if doctest.testmod().failed == 0:
        print("\n*** ALL TESTS PASSED; YOU FOUND SUCCESS! ***\n")
