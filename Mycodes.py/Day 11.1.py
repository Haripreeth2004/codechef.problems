# cook your dish here
t = int(input())
for i in range (t):
    N,A,B = map(int, input().split())
    T =(2*(N/2))+180
  # if N%2==0:
  # else:
 #      T=(((N+1)/2)*2)+180

    Total = 2*T
    Left = A+B
    Dur = Total - Left
    print(round(Dur))
