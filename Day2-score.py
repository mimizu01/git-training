names = []
scores = []

while True:
    name = input("名前を入力してください：")
    
    if not name:
        break
    
    score = input("点数を入力してください：")
    names.append(name)
    scores.append(score)
    
    print("名前：", name)
    print("点数：", score)
    
avg = sum(int(score) for score in scores) / len(scores)
print("平均点：",round(avg, 1),"点")

top_score = 0

for score in scores:
    if int(score) > top_score:
        top_score = int(score)

for name in names:
    if scores[names.index(name)] == str(top_score):
       
        print("最高点：",top_score, "点(",name,"さん)")