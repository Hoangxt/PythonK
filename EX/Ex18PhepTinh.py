# Nhập biểu thức từ bàn phím
print("Nhập số a phếp tính và số b: ")
a, PhepTinh, b = input().split()
# ép kiểu dữ liệu sang số thực
a = float(a)
b = float(b)
# tạo biến lưu kết quả của biểu thức
sum = None
# dùng câu lệnh rẽ nhánh đẻ phân loại phép tính
# lưu kết quả phù hợp
if PhepTinh == '+':
    sum = a + b
elif PhepTinh == '-':
    sum = a - b
elif PhepTinh == '*':
    sum = a * b
elif PhepTinh == '/' or PhepTinh == ':':
    if b == 0:
        print("số thứ 2 phải khác 0")
    else:
        sum = a / b
# in ra kết quả
if sum != None:
    print("{} {} {} = {} ".format(a, PhepTinh, b, sum))
