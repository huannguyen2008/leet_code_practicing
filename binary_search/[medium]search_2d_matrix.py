from typing import List


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    """
    Simply use BS for each row in the matrix baby!
    :param matrix:
    :param target:
    :return:
    """
    n = len(matrix[0])
    for row in matrix:
        l = 0
        r = n - 1
        while l < r:
            m = l + (r - l) // 2
            if row[m] == target:
                return True
            if row[m] > target:
                r = m
            else:
                l = m + 1
        if row[l] == target:
            return True
    return False