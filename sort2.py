students = {}

while True:
    name = input("名前を入力してください：")

    if not name:
        break

    score = int(input("点数を入力してください："))

    students[name] = score

    print("名前：", name)
    print("点数：", score)

# 点数の高い順に並び替え
sorted_students = sorted(
    students.items(),
    key=lambda x:x[1],
    reverse=True
    
)

for name, score in sorted_students:
    print(f"名前: {name} さん")
    print(f"点数: {score} 点")
    print("-----------------------")
    
    