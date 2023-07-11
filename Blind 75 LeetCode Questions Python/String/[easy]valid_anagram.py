def is_anagram(s, t):
    char_counts = {}
    if len(s) != len(t):
        return False
    for i in range(0, len(s)):
        char_counts[s[i]] = char_counts.get(s[i]) + 1 if char_counts.get(s[i]) else 1
        char_counts[t[i]] = char_counts.get(t[i]) - 1 if char_counts.get(t[i]) else -1

    for c in char_counts:
        if char_counts[c] != 0:
            return False

    return True


print(is_anagram('anagram', 'nagaram'))
