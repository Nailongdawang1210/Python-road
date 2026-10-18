#计算1加到100之间偶数的和

sum1 = 0
i = 2
while i <= 100:
    sum1 += i
    i += 2
print(f"1加到100之间偶数的和为：{sum1}")



sum2 = 0
i = 1
while i <= 100:
    if i % 2 == 0:
        sum2 += i
    i += 1
print(f"1加到100之间偶数的和为：{sum2}")
