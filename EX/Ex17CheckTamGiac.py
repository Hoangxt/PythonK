# nhập dc số đo 3 cạnh của tam giác
# sử dụng hàm map() và float để ép kiểu sang số thực
# print("Nhập vào 3 cạnh của tam giác cách nhau bởi khoảng cách:")
# while True:
#     try:
#         a, b, c = map(float, input().split())
#         # dùng câu lệnh rẽ nhánh để check Dk
#         if a + b > c and a + c > b and b + c > a:
#             print("{}, {}, {} là 3 cạnh của tam giác".format(a, b, c))
#         else:
#             print("{}, {}, {} không là 3 cạnh của tam giác".format(a, b, c))
#         break
#     except:
#         print("có lỗi sảy ra !!!")
while True:
    try:
        abc = input('Nhập 3 số cách nhau 1 khoảng trắng: ')
        [a, b, c] = map(float, abc.split(' '))
        assert a > 0 and b > 0 and c > 0
        if a + b > c and a + c > b and b + c > a:
            print("{}, {}, {} là 3 cạnh của một tam giác".format(a,b,c))
        else:
            print("{}, {}, {} không là 3 cạnh của một tam giác".format(a,b,c))
        break
    except ValueError:
        print('Nhập lại đầu vào')
    except AssertionError:
        print('Cạnh phải là số dương')
