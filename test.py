n = int(input())

for i in range(n):
    p = list(map(int, input().split()))
    if p[3] - p[2] == p[2] - p[1] :
        print(f"{p[0]} {p[1]} {p[2]} {p[3]} {p[3]+( p[3] - p[2] )}")
    else:
        print(f"{p[0]} {p[1]} {p[2]} {p[3]} {p[3]*( p[3]//p[2] )}")
