while True:
    try:
        p1 = input("Thông tin bạn đầu tiên là: ")
        p2 = input("Thông tin bạn thứ hai là: ")
        [name1, age1] = p1.split(' ')
        age1 = int(age1)
        [name2, age2] = p2.split(' ')
        age2 = int(age2)
        if age1 > age2:
            print("Bạn", name1,  "cao hơn bạn", name2)
        elif age1 == age2:
            print("Hai bạn cao bằng nhau")
        else:
            print("Bạn", name2,  "cao hơn bạn", name1)
        break
    except ValueError:
        print('Lỗi nhập liệu, nhập lại \n')
