# import csv

# with open('Roster.csv', encoding='utf-8-sig') as f: 
#     reader = csv.DictReader(f)
#     for row in reader:
#        print(f"社員番号:{number} 氏名:{name}")

import csv

with open('Roster.csv', encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"社員番号{row['number']}番 氏名:{row['name']}")