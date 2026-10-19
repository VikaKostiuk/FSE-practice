x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
c1 = (x1 + y1) % 2
c2 = (x2 + y2) % 2

if c1 == c2:
    print("YES")
    if c1 == 0:
        print("White")
    else:
        print("Black")
else:
    print("NO")