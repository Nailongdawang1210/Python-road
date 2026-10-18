a = int(input("请输入三角形的第一个边长： "))
b = int(input("请输入三角形的第二个边长： "))
c = int(input("请输入三角形的第三个边长： "))
if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("这是一个等边三角形")
    elif a == b or b == c or a == c:
        print("这是一个等腰三角形")
    else:
        print("这是一个不等边三角形")
else:
    print("这三条边无法构成三角形")