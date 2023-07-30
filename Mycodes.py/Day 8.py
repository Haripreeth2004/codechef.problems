# cook your dish here
t = int(input())
for i in range (t):
    NM = input()
    N, M = map(int, NM.split())
    Total = (N*5) + (M*7)
    print(Total)
