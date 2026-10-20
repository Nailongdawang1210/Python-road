# def area_a (l,w):
    # return l * w
# print(area_a(5, 10))
# def area_triangle(base, height):
    # return round((base * height)/2,1)
# print(area_triangle(5, 10))
# def count_str(s):
    # sum = 0
    # for item in s:
        # match item:
            # case "a" | "e" | "i" | "o" | "u"| "A" | "E" | "I" | "O" | "U":
                # sum += 1
    # return sum
# s = input("请输入一个字符串： ")
# print("元音字母的个数为：", count_str(s))
def study(list):
    """
    计算成绩的最高分、最低分和平均分
    :param list: 成绩列表
    :return: 最高分、最低分、平均分
    """
    max_score = max(list)
    min_score = min(list)
    avg_score = round(sum(list) / len(list), 1)
    return max_score, min_score, avg_score
scores = [int(x) for x in input("请输入成绩列表（用逗号分隔）： ").split(",")] 

max_score, min_score, avg_score = study(scores)
print("最高分为：", max_score)  
print("最低分为：", min_score)
print("平均分为：", avg_score)
str1 = "a,s,g,j,t"
str2 = str1.split(",")
print(str2)
print(type(str2))