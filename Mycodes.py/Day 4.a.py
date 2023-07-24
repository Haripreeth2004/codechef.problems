# cook your dish here
T = int(input())
for i in range (T):
    XH = input()
    X, H = map(int, XH.split())
    print("YES" if X >= H else "NO")
   
