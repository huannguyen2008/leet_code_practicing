from typing import List


def count_negatives(grid: List[List[int]]) -> int:
    """
    - m = len(grid), n = len() of each arr in grid.

    - First approach: For every row in matrix, we use binary search to find a negative number, then add all the element
    from that one to the right into result
    O = m x log(n)

    - Second approach: Go from bottom left item, check if it is a negative number or not. If yes, add all the element
    from that one to the right into result. If no, then go up to the next row.
    O = m + n
    """
    result = 0

    # rows = len(grid)
    # for i in range(0, rows):
    #     l = 0
    #     r = len(grid[i]) - 1

    #     while l < r:
    #         m = l + (r - l) // 2

    #         if grid[i][m] >= 0:
    #             l = m + 1
    #         if grid[i][m] < 0:
    #             r = m

    #     if grid[i][l] < 0:
    #         result += len(grid[i]) - l

    # return result
    m = len(grid)
    n = len(grid[0])

    i = m - 1
    j = 0

    while i >= 0 and j < n:
        if grid[i][j] < 0:
            result += n - j
            i -= 1
        else:
            j += 1

    return result

print(count_negatives([[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))
