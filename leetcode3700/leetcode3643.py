
from typing import List


class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:

        t = k
        for i in range(x, x+ k//2):
            for j in range(y, y + k):
                tmp = grid[i][j]
                grid[i][j] = grid[i + t - 1][j]
                grid[i + t - 1][j] = tmp
            t -= 2
        return grid


if __name__ == '__main__':
    grid = [[14,3,18,16],[2,14,11,20],[19,19,4,15],[11,15,18,6]]
    sol = Solution()
    sol.reverseSubmatrix(grid, 0, 0, 4)
    print(grid)