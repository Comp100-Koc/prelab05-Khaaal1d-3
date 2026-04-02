def remove_adjacent_duplicates(s):
    changed = True

    while changed:
        changed = False
        i = 0

        while i < len(s) - 1:
            if s[i] == s[i + 1]:
                s = s[:i] + s[i + 2:]
                changed = True
                i = 0
            else:
                i += 1

    return s
