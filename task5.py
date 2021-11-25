def is_sorted(t):
    if sorted(t) == t:
        return True
    else:
        return False


print('Введите числовой ряд: ')
t = input(' ').split()
print(is_sorted(t))