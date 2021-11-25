def chop(t):
    t.pop(len(t) - 1)
    t.pop(0)


print('Введите чимловой ряд: ')
t = input(' ').split()
chop(t)
print(t)
