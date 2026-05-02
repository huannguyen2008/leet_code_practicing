def longest_common_prefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    lcp = strs[0]
    if len(strs) == 0:
        return ""
    for i in strs[1:]:
        while not i.startswith(lcp):
            lcp = lcp[:-1]
    return lcp


print(longest_common_prefix(["flower", "flow", "flight"]))
