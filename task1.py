def nested_sum(t):
    summary = 0
    for a in t:
        summary += sum(a)
    return summary
    print('Введите числа: ', nested_sum())


t = [[0 for i in range(2)] for b in range(2)]
print('Введите числа: ')
for i in range(2):
    row = input(' ').split()
    for b in range(2):
        t[i][b] = int(row[b])

print('Ссумма чисел = ', nested_sum(t))
