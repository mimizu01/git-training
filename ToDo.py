ToDo_list = ["1: 追加", "2: 表示", "3: 削除","4: CSV出力"]
save_list = []


while True:
    print(ToDo_list)
    input_num = input("番号を入力してください：")
    
    if not input_num:
        break
    
    elif input_num == "1":
        
        add_item = input("追加する内容を入力してください：")
        
        save_list.append(add_item)
         
    elif input_num == "2":
        
        for index,item in enumerate(save_list,start = 1):#大事
            print(f"{index}.{item}")
            
    elif input_num == "3":
        
        input_rm = int(input("削除したい番号を入力してください："))
        
        delete_index = input_rm - 1
        
        save_list.pop(delete_index)
    
    elif input_num == "4":
        
        with open("ToDo_list.csv","w") as file: #大事
        
            for item in save_list:
                
                file.write(item + "\n")
        
        #file.close()
  
for