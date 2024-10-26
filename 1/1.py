x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
x = int(input())
y = int(input())

lens = {
    "NW" : ((x1 - x)**2 + (y2 - y)**2)**0.5,
    "N" : 0,
    "NE" : ((x2 - x)**2 + (y2 - y)**2)**0.5,
    "E" : 0,
    "SE" : ((x2 - x)**2 + (y1 - y)**2)**0.5,
    "S" : 0,
    "SW" : ((x1 - x)**2 + (y1 - y)**2)**0.5,
    "W" : 0,
}
if x < x1 or x > x2:
    lens["N"] = 10**10
else:
    lens["N"] = abs(y - y2)

if y > y2 or y < y1:
    lens["E"] = 10**10
else:
    lens["E"] = abs(x - x2)

if x < x1 or x > x2:
    lens["S"] = 10**10
else:
    lens["S"] = abs(y1 - y)

if y > y2 or y < y1:
    lens["W"] = 10**10
else:
    lens["W"] = abs(x1- x)
print(lens)
print(min(lens, key=lens.get))