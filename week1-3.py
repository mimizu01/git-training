score = int(input("点数:"))

if score < 0 or score > 100:
    print("エラー")
elif score >= 80:
    print("A")
elif score >= 60:
    print("B")
else:
    print("C")
