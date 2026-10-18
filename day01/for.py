
# sum = 0
# for i in range(102, 500, 3):
    # sum += i
# print(f"100到500之间能被3整除的数的和为：{sum}")
# for i in range(1, 10):
    # for j in range(1,i+1):
        # print(f"{j} * {i} = {i*j}", end="\t")
    # print()

# 


for i in range(8):
    if i % 2 == 0:
        
        for j in range(8):
            if j % 2 == 0:
                print("■", end=" ")
            else:
                print("□", end=" ")
             
        print()
    else:
        for j in range(8):
            if j % 2 == 0:
                print("□", end=" ")
            else:
                print("■", end=" ")
             
        print()        
