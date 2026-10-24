class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Count islands of '1's connected horizontally or vertically.

        Args:
            grid: Rectangular grid of '1' (land) and '0' (water). May be empty.

        Returns:
            Number of islands.

        Complexity:
            Time O(m * n), space O(m * n).
        """
        if not grid:
            return 0

        row_count = len(grid)
        column_count = len(grid[0])

        directions = ((1, 0), (-1, 0), (0, 1), (0, -1))  # down, up, right, left
        visited_cells = set()
        island_count = 0

        for row in range(row_count):
            for column in range(column_count):
                # Skip water and cells of islands already counted.
                if grid[row][column] != '1' or (row, column) in visited_cells:
                    continue

                island_count += 1

                # Iterative DFS: mark the whole island as visited.
                cells_to_explore = [(row, column)]
                visited_cells.add((row, column))  # mark on push

                while cells_to_explore:
                    current_row, current_column = cells_to_explore.pop()

                    for row_step, column_step in directions:
                        neighbor_row = current_row + row_step
                        neighbor_column = current_column + column_step
                        neighbor = (neighbor_row, neighbor_column)

                        # Bounds check first: negative indices wrap in Python.
                        if (
                            0 <= neighbor_row < row_count
                            and 0 <= neighbor_column < column_count
                            and grid[neighbor_row][neighbor_column] == '1'
                            and neighbor not in visited_cells
                        ):
                            visited_cells.add(neighbor)
                            cells_to_explore.append(neighbor)

        return island_count