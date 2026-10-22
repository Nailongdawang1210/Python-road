def Naicha(*args,**kwargs):
    print("益和糖")
    if kwargs["order"] == 1:
        if args[0] == 1:
            print("常温")
        else:
            print("加冰")
                
        print(f"选择了{args[1]}分糖")
Naicha(int(input("是否加冰 ")),int(input("选择几分糖 ")),order = int(input("是否点餐(0/1) ")) )
print("益和糖")