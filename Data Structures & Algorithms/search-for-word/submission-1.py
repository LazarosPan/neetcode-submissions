class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Determine whether `word` can be traced in `board` through horizontally
        or vertically adjacent cells, using each cell at most once per path.

        Approach:
            Iterative DFS with backtracking. For every cell matching word[0],
            keep an explicit stack (`path`) of cells matched so far. Each stack
            entry also remembers which of the 4 directions to try next, so we
            can resume exploring after backtracking.

        Arguments:
            board: 2-D grid of letters (list of lists of single characters).
            word: target string.

        Returns:
            True if the word can be formed in the grid, otherwise False.

        Complexity:
            Time:  O(m * 4^n), m = number of cells, n = len(word).
            Space: O(n) for the path stack and the visited set.
        """
        total_rows, total_cols = len(board), len(board[0])

        # Quick prune: the word cannot fit if it is longer than the board.
        if len(word) > total_rows * total_cols:
            return False

        # Down, up, right, left.
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for start_row in range(total_rows):
            for start_col in range(total_cols):
                # Only cells matching the first letter can start a path.
                if board[start_row][start_col] != word[0]:
                    continue

                # Each stack entry: [row, col, next_direction_index_to_try].
                # len(path) == number of letters matched so far.
                path = [[start_row, start_col, 0]]
                # Cells in the CURRENT path only (visited is per path, not global).
                cells_in_path = {(start_row, start_col)}

                while path:
                    # Success: every letter of the word has been matched.
                    if len(path) == len(word):
                        return True

                    current_row, current_col, next_direction_index = path[-1]

                    # All 4 neighbors tried: backtrack (undo this cell).
                    if next_direction_index == len(directions):
                        path.pop()
                        cells_in_path.remove((current_row, current_col))
                        continue

                    # Advance this cell's direction pointer so that, after
                    # backtracking to it, we try the next neighbor.
                    path[-1][2] += 1

                    row_step, col_step = directions[next_direction_index]
                    neighbor_row = current_row + row_step
                    neighbor_col = current_col + col_step

                    # The neighbor extends the path only if it is inside the
                    # board, unused in this path, and equals the next letter
                    # needed (word[len(path)]).
                    if (
                        0 <= neighbor_row < total_rows
                        and 0 <= neighbor_col < total_cols
                        and (neighbor_row, neighbor_col) not in cells_in_path
                        and board[neighbor_row][neighbor_col] == word[len(path)]
                    ):
                        path.append([neighbor_row, neighbor_col, 0])
                        cells_in_path.add((neighbor_row, neighbor_col))

        # No starting cell led to a complete match.
        return False