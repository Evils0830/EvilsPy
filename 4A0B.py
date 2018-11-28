
import random
#import numpy as np

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 數字庫
Dig4 = random.sample(arr, 4)

#aList = []  # 每回嘗試紀錄
result = []  # 每回判定結果
count = 9  # 遊玩次數

print("我想想... 我想好了!")
BringOn = input("猜一組不重複的四位數字: ")

while BringOn != Dig4: #相同就結束
    number = [int(x) for x in str(BringOn)]
    same = 0
    if len(BringOn) == 4: #檢查四位數字
        for i in range(4):
            for j in range(4):
                if number[i] == number[j]: #檢查重複數字
                    if i == j: #重複則跳過
                        continue
                    else:
                        same += 1
        if same == 0: #不重複才計數
            #aList.append(BringOn)
            count -= 1
            if count <= 0:
                print("喔喔, 再練練吧, 下次再來!")
                print("讓你輸得心服口服, 答案是"+str(Dig4))
                quit()
            else:
                if number == Dig4: #結束遊戲
                    print("恭喜你猜對了, 遊戲結束! 4A0B ")
                    quit()
                else:
                    print("再猜一次,剩下" + str(count) + "次")
                    An = 0
                    Bn = 0
                    antic = 0
                    for i in range(4):
                        if number[i] == Dig4[i]: #檢查位置相同的數字
                            An += 1
                        for j in range(4):
                            if number[i] == Dig4[j]: #檢查相同的數字
                                Bn += 1
                    Bns = Bn - An #相減得到B
                    antic = 9 - count
                    result.append(str(antic) + ". " + BringOn + " > " + str(An)+"A"+str(Bns)+"B")
                    for row in result:
                        print(row)
                    #print(Dig4)
                    BringOn = input("猜一組不重複的四位數字: ")
        else:
            print("數字重複! 你這樣一輩子都猜不到喔!")
            BringOn = input("猜一組不重複的四位數字: ")
    else:
        print("請輸入一組四位數字!")
        BringOn = input("猜一組不重複的四位數字: ")
else:
    print("恭喜你猜對了, 要再來一次?")
