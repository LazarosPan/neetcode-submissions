class NumMatrix:
    """
    2D prefix-sum structure for immutable matrices.

    P[i][j] = sum of matrix[0..i-1][0..j-1]  (an extra zero row/column
    is added so queries at the border need no special cases).

    Time:  __init__ O(m*n), sumRegion O(1)
    Space: O(m*n)
    """

    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        # (m+1) x (n+1) table; row 0 and column 0 stay 0 as the "empty" prefix
        self.P = [[0] * (n + 1) for _ in range(m + 1)]

        for r in range(m):
            row_run = 0  # running sum of the current row, from column 0 to c
            for c in range(n):
                row_run += matrix[r][c]
                # rectangle (0,0)->(r,c) = rectangle ending in the row above
                #                          + this row's running sum
                self.P[r + 1][c + 1] = self.P[r][c + 1] + row_run

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """Sum of the rectangle (row1,col1)->(row2,col2), inclusive, in O(1)."""
        P = self.P
        # P is shifted by +1, so the "+1" is applied to the bottom-right indices
        # and row1/col1 index directly to the row/column just before the rectangle.
        return (
            P[row2 + 1][col2 + 1]    # everything from (0,0) to bottom-right
            - P[row1][col2 + 1]      # remove the strip above the rectangle
            - P[row2 + 1][col1]      # remove the strip left of the rectangle
            + P[row1][col1]          # top-left corner was removed twice: add back
        )

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)