from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num_islands = 0

        def explore_island(grid: List[List[str]], row, col):
            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[row]):
                return
            if grid[row][col] == "0":
                return
            grid[row][col] = "0"
            explore_island(grid, row + 1, col)
            explore_island(grid, row - 1, col)
            explore_island(grid, row, col + 1)
            explore_island(grid, row, col - 1)

        for row in range(len(grid)):
            for col in range(len(grid[row])):
                # is it an island?
                if grid[row][col] == "1":
                    # explore the island and turn it to water! also increment num islands
                    num_islands += 1
                    explore_island(grid, row, col)

        return num_islands
    

def main():
    grid=[["1","1","0","0","1"],["1","1","0","0","1"],["0","0","1","0","0"],["0","0","0","1","1"]]
    print(len(grid))
    print(len(grid[0]))
    sol = Solution()
    print(sol.numIslands(grid))

if __name__ == "__main__":
    main()