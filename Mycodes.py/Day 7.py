t = int(input ())
for i in range (t):
    B = 0
    F = 0
    k = int(input ())
    for j in range (1,k+1):
        K = j%2
        if (K==0):
            B = B+1
        else :
            F = F+3
    Total = F-B
    print(Total)
