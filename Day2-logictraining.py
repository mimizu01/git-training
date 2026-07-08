import random

num = random.randint(1, 100)

count = 0

while True :
    
    try:
        number = int(input("1~100の数字を入力してください："))

        if number < 1 or number > 100:
            print("1~100の数字を入力してください")
            continue

    except ValueError:
        print("無効な入力です。数字を入力してください。")
        continue
    
    count += 1
    
    if number == num:
        print("正解です！")
        print("繰り返した回数：", count)
        break
    
    elif number > num:
        print("もっと小さいです")
    else :
        print("もっと大きいです")
        
       
              