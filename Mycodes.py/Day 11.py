# cook your dish here
t = int(input())
for i in range(t):
    N,M = map(int,input().split())
    Total = M * 6* 6
    print("YES" if Total >= N else "NO")
    
