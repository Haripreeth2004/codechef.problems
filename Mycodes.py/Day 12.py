# cook your dish here
t = int(input())
for i in range(t):
    KL = input()
    List = [j for j in KL]
    IL = [int(s) for s in List]
    T = 0
    for k in IL:
        if(k == 4):
            T = T+1
    print(T)
