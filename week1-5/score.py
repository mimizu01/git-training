import csv

def evaluate(avg):
    if avg >= 80:
        return "A"
    elif avg >= 65:
        return "B"
    else:
        return "C"

with open('score.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    
    for row in reader:
        
        total = (
            int(row['kokugo']) + int(row['eigo']) + int(row['sugaku']) + int(row['syakai']) + int(row['rika'])
        )

        avg = total / 5        
        result = evaluate(avg)
        print(f"{row['name']}：平均 = {int(avg)} 評価 = {result}")

   