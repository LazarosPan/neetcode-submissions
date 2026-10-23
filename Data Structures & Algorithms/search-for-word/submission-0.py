class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Determine whether `word` can be traced in `board` through horizontally
        or vertically adjacent cells, using each cell at most once per path.

        Approach:
            Recursive DFS with backtracking. From every cell, try to match the
            word letter by letter. A cell is temporarily marked as visited
            while it is part of the current path, then restored on return.

        Arguments:
            board: 2-D grid of letters (list of lists of single characters).
            word: target string.

        Returns:
            True if the word can be formed in the grid, otherwise False.

        Complexity:
            Time:  O(m * 4^n), m = number of cells, n = len(word).
            Space: O(n) recursion depth (board is mutated in place, no extra set).
        """
        total_rows, total_cols = len(board), len(board[0])

        # Quick prune: the word cannot fit if it is longer than the board.
        if len(word) > total_rows * total_cols:
            return False

        def matches_from(row: int, col: int, matched_count: int) -> bool:
            """
            Try to match word[matched_count:] starting at (row, col).
            `matched_count` is how many letters are already matched, which is
            also the index of the letter this cell must equal.
            """
            # Success: every letter has been matched.
            # Must be checked BEFORE bounds/indexing, since word[matched_count]
            # would be out of range at this point.
            if matched_count == len(word):
                return True

            # Failure: outside the board, or letter differs from the one needed.
            # Bounds are checked first so that `or` short-circuits before
            # board[row][col] is accessed with an invalid index.
            # Cells already in the path hold '#', which never equals a letter,
            # so they are rejected here too.
            if (
                row < 0 or row >= total_rows
                or col < 0 or col >= total_cols
                or board[row][col] != word[matched_count]
            ):
                return False

            # Choose: mark this cell as used in the current path.
            original_letter = board[row][col]
            board[row][col] = '#'

            # Explore: try all 4 neighbors for the next letter.
            # `or` stops at the first successful direction.
            found = (
                matches_from(row + 1, col, matched_count + 1)      # down
                or matches_from(row - 1, col, matched_count + 1)   # up
                or matches_from(row, col + 1, matched_count + 1)   # right
                or matches_from(row, col - 1, matched_count + 1)   # left
            )

            # Unchoose (backtrack): restore the letter so other paths can use it.
            board[row][col] = original_letter

            return found

        # The path may start at any cell.
        for start_row in range(total_rows):
            for start_col in range(total_cols):
                if matches_from(start_row, start_col, 0):
                    return True

        # No starting cell led to a complete match.
        return False