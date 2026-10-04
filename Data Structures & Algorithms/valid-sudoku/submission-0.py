from collections import defaultdict

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # GIVEN:
        # 9x9 board
        # 1. row -> 1-9 no duplicates
        # 2. column -> 1-9 no duplicates
        # 3. 3x3 sub-boxes -> 1-9 no duplicates
        # return True if valid else False

        # CONSTRAINTS:
        # board.length == 9
        # board[i].length == 9
        # board[i][j] is a digit 1-9 or '.'.

        # QUESTIONS:
        # in the example why its true since there are no numbers at all and have "." instead
        # answer: valid != solved. its valid to start solving it.
        
        # IDEAS:
        # no duplicates -> set()
        # ignore "." because its a valid signal lets say
        # use a dictionary to track the existance of numbers are already in a row/column/subbox
        # how to split the dict for row/column/subbox count?
        # box coordinates is row//3 and col//3

        rows = defaultdict(set)
        columns = defaultdict(set)
        boxes = defaultdict(set)

        for row in range(9):
            for column in range(9):
                value = board[row][column]

                if value == ".":
                    continue

                box = (row // 3, column // 3)

                if (
                    value in rows[row]
                    or value in columns[column]
                    or value in boxes[box]
                ):
                    return False

                rows[row].add(value)
                columns[column].add(value)
                boxes[box].add(value)

        return True