# for i in range(1,8):
#     for j in range(1,i+1):
#         print(i,end="")
#     print("\r")

b=0
for i in  range(5,0,-1):
    b+=1
    for j in range(1,i+1):
        print(b,end="")
    print("\r")