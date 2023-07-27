# cook your dish here
A,B,X,Y = map(int, input().split())
R = 2*X + Y
M = 2*A + B
if (R>M):
    print("Ronaldo")
elif (R==M):
    print("Equal")
else :
    print("Messi")
