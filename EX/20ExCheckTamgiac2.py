# Nhap so do ba canh tu ban phim
# Su dung ham map() va float de ep kieu du lieu sang so thuc
while True:
    try:
        print("Nhập 3 số bất kì > 0: ")
        a, b, c = map(float, input().split())
        # Dung cau lenh re nhanh de kiem tra dieu kien cac tam giac
        # Kiem tra dieu kien la ba canh cua tam giac
        assert a > 0 and b > 0 and c > 0
        if a+b > c and a+c > b and b+c > a:
            # Kiem tra tam giac vuong
            if a*a == b*b+c*c or b*b == a*a+c*c or c*c == a*a+b*b:
                loaiTamGiac = 'Vuông'
            # Kiem tra tam giac deu
            elif a == b and b == c:
                loaiTamGiac = 'Đều'
            # Kiem tra tam giac can
            elif a == b or a == c or b == c:
                loaiTamGiac = 'Cân'
            # Kiem tra tam giac tu
            elif a*a > b*b+c*c or b*b > a*a+c*c or c*c > a*a+b*b:
                loaiTamGiac = 'Tù'
            # Cac truong hop con lai la tam giac nhon
            else:
                loaiTamGiac = 'Nhọn'
            # Xuat thong bao theo yeu cau
            print('{}, {}, {} Là 3 cạnh của 1 tam giác {}'.format(
                a, b, c, loaiTamGiac))
        else:
            print("{}, {}, {} Không phải là 3 cạnh cuẩ 1 tam giác ".format(a, b, c))
        break
    except ValueError:
        print('Nhập lại đầu vào')
    except AssertionError:
        print('Cạnh phải là số dương')
