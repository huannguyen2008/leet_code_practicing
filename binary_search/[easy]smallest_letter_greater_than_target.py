from typing import List


def next_greatest_letter(letters: List[str], target: str) -> str:
    l = 0
    r = len(letters) - 1

    while l < r:
        m = l + (r - l) // 2
        if letters[m] <= target:
            l = m + 1
        if letters[m] > target:
            r = m
    return letters[l] if letters[l] > target else letters[0]
