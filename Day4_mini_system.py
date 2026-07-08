import sys

save_itemlist = []
save_pricelist = []
save_numlist = []


def addItem():  # 商品追加

    item = input("登録したい商品名を入力してください > ")
    
    try:
        price = int(input("価格を入力してください > "))
        num = int(input("在庫数を入力してください > "))
        
    except:
        print("エラーが発生しました。")
        return

    save_itemlist.append(item)
    save_pricelist.append(price)
    save_numlist.append(num)
    print("---------------登録しました！-----------------")
    
    
def addList():  # 一覧表示

    print("《 商品一覧 》")

    for index, (item, price, num) in enumerate(
        zip(save_itemlist, save_pricelist, save_numlist), start=1
    ):

        print(f"{index}.商品：{item}　価格：{price}円　在庫数：{num}個")


def addDelete():  # 削除処理
    
    delete = int(input("削除したい商品番号を入力してください > "))
    
    delete_index = delete - 1
    save_itemlist.pop(delete_index)
    save_pricelist.pop(delete_index)
    save_numlist.pop(delete_index)
    
    print("---------------削除しました！-----------------")
    
    
def addTotal(): #集計表示
    
    print("《 集計 》")
    
    number_item = 0 #登録商品数
        
    number_item = len(save_itemlist)
        
    print("登録商品数：" ,number_item,"個")
    
    
    avg_price = 0   #平均価格 
        
    avg_price = sum(int(price) for price in save_pricelist) / len(save_pricelist)

    print(f"平均価格：",round(avg_price, 1),"円")
    
    top_price = 0 #最高価格の商品名と価格
    
    for price in save_pricelist:
        if int(price) > top_price:
            top_price = int(price)

    for item, price in zip(save_itemlist, save_pricelist):
        
        if save_pricelist[save_itemlist.index(item)] == top_price:
            
            print("最高価格：", item, "(", top_price, "円)")
    

    num_total = 0 #在庫合計数
    
    for num in save_numlist:
        num_total += num 
    print(f"在庫合計数：{num_total}個")
            
def addSort(): #降順に並び替え

    pairs = list(zip(save_itemlist, save_pricelist))
    pairs.sort(
        key=lambda x: x[1], 
        reverse=True
    )    
    
    for item, price in pairs:
        print("価格：", item, "(", price, "円)")
        
    
print("=== ミニショップ 在庫管理システム === ")

while True:
    print()
    print("1:商品追加 2:一覧表示 3:商品削除 4:集計表示 5:価格順に並べる 0:終了")
    input_num = input("番号を入力してください：")

    if not input_num or input_num == "0":
        break

    elif input_num == "1":
        addItem()

    elif input_num == "2":
        addList()

    elif input_num == "3":
        addDelete()
        
    elif input_num == "4":
        addTotal()
        
    elif input_num == "5":
        addSort()
