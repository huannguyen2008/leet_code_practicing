from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    We go from the top-right corner to bottom-left corner. Not really a BS ...
    :param matrix:
    :param target:
    :return:
    """
    m = len(matrix)
    n = len(matrix[0])

    i = 0
    j = n - 1

    while i < m and j >= 0:
        cur = matrix[i][j]
        if cur == target:
            return True
        if cur > target:
            j = j - 1
        if cur < target:
            i = i + 1

    return False