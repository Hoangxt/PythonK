# Tính tổng của 1 dãy số

while True:
    try:
        n = input('Nhập vào các dãy số cách nhau bởi khoảng trắng: ')
        n = n.split(' ')
        n = map(int, n)
        sumN = sum(n)
        print("Tổng của dãy số: ", sumN)
        break
    except:
        print('Hãy nhập lại')
