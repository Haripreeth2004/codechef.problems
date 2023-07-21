testcase = int(input())
for i in range (testcase):
    jerrytom = input()
    jerry, tom = map(int, jerrytom.split())
    if (tom>jerry):
        print("YES")
    else:
        print("NO")
    
