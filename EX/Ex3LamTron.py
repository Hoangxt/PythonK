# làm tròn số
# soA = float(input())
# soB = int(input())
# print('{0:.{1}f}'.format(soA, soB))
while True:
    try:
        n = float(input("Nhập số nguyên dạng thập phân: "))
        r = int(input("Nhập số chữ số sau dấu phẩy: "))
        print(round(n, r))
        break
    except:
        print("Xin mời nhập lại đê")
