scoreList = []
while True:
    print("1.查成績")
    print("2.儲存成績")
    print("3.跳出系統")
    selection = input('請輸入功能')
    if selection =='1':
        score = int(input('請輸入成績'))
        if score >=60:
            if score<90:
                print('good')
            else:
                print('very good')
        else:
            print('fail')
    elif selection == '2':
        score = int(input('請輸入成績'))
        scoreList.append(score)
        print("全班成績表",scoreList)
    elif selection == '3':
        break
    else:
        print("Error")

