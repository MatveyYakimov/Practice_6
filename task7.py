def is_duplicate(s):
    if len(s) != len(set(s)):
        return True
    return False


s = input(' ').split()
print(is_duplicate(s))
