a = int(input())
b = int(input())
c = int(input())
d = int(input())

sum1 = max(a, b) + 1 + 1
sum2 = 1 + max(c, d) + 1
sum3 = a + 1 + c + 1
sum4 = b + 1 + d + 1

if a == 0:
    if max(c, d) == d:
        print(1, c + 1)
    else:
        print(1, max(c, d) + 1)
elif b == 0:
    if max(c, d) == c:
        print(1, d + 1)
    else:
        print(1, max(c, d) + 1)
elif c == 0:
    if max(a, b) == b:
        print(a + 1, 1)
    else:
        print(max(a, b) + 1, 1)
elif d == 0:
    if max(a, b) == a:
        print(b + 1, 1)
    else:
        print(max(a, b) + 1, 1)

elif min(sum1, sum2, sum3, sum4) == sum1:
    print(max(a, b) + 1, 1)
elif min(sum1, sum2, sum3, sum4) == sum2:
    print(1, max(c, d) + 1)
elif  min(sum1, sum2, sum3, sum4) == sum3:
    print(a + 1, c + 1)
elif min(sum1, sum2, sum3, sum4) == sum4:
    print(b + 1, d + 1)