# # import thư viện math
# import math
# # nhập 3 hệ số từ bàn phím
# # ép kiểu về float dùng hàm map
# isOK = False
# try:
#     a, b, c = map(float, input().split())
# except:
#     print("có lỗi dữ liệu đầu vào")
# if isOK:
#     # dùng câu lệnh rẽ nhánh để check
#     # xuất thông báo cho từng TH
#     if a == 0:
#         if b == 0:
#             if c == 0:
#                 print("Phương trình có vô số nghiệm")
#             else:
#                 print("Phương trình vô nghiệm")
#         else:
#             print("Phương trình có 1 nghiệm duy nhất: \nx = {}".format(-c/b))
#     else:
#         # tính delta
#         delta = b * b - 4 * a * c
#         # ktra các Th của delta
#         if delta > 0:
#             x1 = float((-b + math.sqrt(delta)) / (2 * a))
#             x2 = float((-b - math.sqrt(delta)) / (2 * a))
#             print(
#                 "Phương trình có 2 nghiệm phân biệt là: \n x1 = {} \n x2 = {}".format(x1, x2))
#         elif detal == 0:
#             x = -b / (2 * a)
#             print("Phương trình có nghiệm ghép: \nx1 = x2 = {}".format(x))
#         else:
#             print("Phương trình vô nghiệm")
import math 
while True:
    try:
        dulieu = input('Nhập giá trị hệ số a b c cách nhau bởi khoảng trắng: ')
        [a, b, c] = map(float,dulieu.split(' '))

        if a == 0:
            if b == 0:
                if c ==0:
                    print('Phương trình có vô số nghiệm')
                else:
                    print('Phương trình vô nghiệm')
            else:
                x = -c/b
                print('Phương trình có  nghiệm duy nhất là %.2f'%(x))
        else:
            denta = b*b -4*a*c
            if denta < 0:
                print('Phương trình vô nghiệm')
            elif denta == 0:
                x = -b/(2*a)
                print('Phương trình có nghiệm kép là %.2f'%(x))
            else:
                x1 = (-b-math.sqrt(denta))/(2*a)
                x2 = (-b+math.sqrt(denta))/(2*a)
                print('Phương trình có 2 nhiệm, nghiệm thứ nhất là %.2f, nghiệm thứ 2 là %.2f'%(x1,x2))
        break
    except ValueError:
        print('Sai định dạng đầu vào, nhập lại...')