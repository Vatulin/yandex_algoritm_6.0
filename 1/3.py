n = int(input())
table = []
for i in range(n):
    table.append(input())

cnt_vertical = 0
cnt_horizontal = 0

#Считаем кол-во горизонтальных линий
for line in table:
    cnt = 0
    line = line.split('.')
    for i in line:
        if len(i) != 0: cnt += 1
    if cnt == 1: cnt_horizontal += 1

#Считаем кол-во вертикальных линий
for i in range(n):
    line = ""
    cnt = 0
    for j in range(n):
        line += table[j][i]
    for symbol in line.split('.'):
        if len(symbol) != 0: cnt += 1
    if cnt == 1: cnt_vertical += 1

if (cnt_vertical == 0) and (cnt_horizontal == 1):
    print('I')
elif (cnt_vertical == 2) and (cnt_horizontal == 1):
    print('H')
elif (cnt_vertical == 2) and (cnt_horizontal == 2):
    print('P')
elif (cnt_vertical == 1) and (cnt_horizontal == 2):
    print('L')
else:
    print('X')