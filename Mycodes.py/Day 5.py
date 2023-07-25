# cook your dish here
T = int(input())
for i in range(T):
    FF = input()
    F ,f = map(int, FF.split())
    x = f*10
    print("YES" if x<F else "NO")
