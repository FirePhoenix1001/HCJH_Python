import math

a, b, c = map(int, input().split())
D = b ** 2 - 4*a*c
if D>0:
    root1 = int((-b+math.sqrt(D) )/(2*a) )
    root2= int((-b-math.sqrt(D) )/(2*a) )
    print("Two different roots x1={root1}, x2={root2}")
elif D == 0:
    root = int((-b+math.sqrt(D) )/(2*a) )
    print("Two same roots x={root}")

else:
    print("No real root")