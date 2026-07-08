import csv #宣言

total_sum = 0

with open('sales.csv', encoding='utf-8-sig') as f: #csvファイルを開く
    reader = csv.DictReader(f) 
    print(reader)
    for row in reader:
        total = int(row['quantity']) * int(row['unit_price']) 
        total_sum += total 
        print(f"{row['product']}：{total}")

print(f"全体の合計：{total_sum}円")


# quantity → 数量
# unit_price → 単価
# int() → 文字→数字に変換
