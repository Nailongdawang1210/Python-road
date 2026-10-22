# def Love(age):
#     if age == 520:
#         return "喜欢王文婧"
#     elif age == 1314:
#         return "爱王文婧一生一世"
#     elif age == 2017:
#         return "王文婧，你是我心中的唯一"
#     elif age == 250:
#         return "舔狗"
#     else:
#         return "她真的不一样"
# Love_W = input("请输入你想要表达的爱意数字：")
# print(Love(int(Love_W)))
# tuple1 = (1, 2, 3, 4, 5)
# set1 = {1, 2, 3, 4, 5}
# set1.add(6)
# print(set1)
# set1.remove(3)
# print(set1)
# def math(num_list):
    # math_max = max(num_list)
    # return math_max
# print(math([1, 2, 3, 4, 5]))
# def person(name, age,address,tel = 10086):
#     print("姓名：", name)
#     print("年龄：", age)
#     print("地址：", address)
#     print("电话：", tel)
#     return name,age,address,tel
# print(person("王文婧",18,"Myheart" ))
# def math(*args,**kwargs):
    
#         max_num = max(args)
#         avg = round(sum(args)/len(args),kwargs["round"])
#         print(type(kwargs["print"]))
#         if kwargs["print"]  :
             
#              print(max_num)
#              print(avg)
#         return max_num,avg
      
# print(math(333,555,444,777,print = False,round = 2))
# print((False))
def add(x,y):
    return x + y
def clac(x,y,opea):
    return(opea(x,y))
print(clac(5,6,add))
a: list[int] = [1,2,3,4]   
print(a)
a.append("5")
print(a)