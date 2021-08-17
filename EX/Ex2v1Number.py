# giatri = input()
# try:
#     sothapphan = int(giatri)
#     print("Số thập phân  %d trong hệ bát phân là %o " %
#           (sothapphan, sothapphan))
# except:
#     print("Định dạng đầu vào không hợp lệ")
while True:
    try:
        a = int(input('Nhập số nguyên dạng thập phân: '))
        print('Số thập phân %d ở dạng bát phân là %o' % (a, a))
        break
    except:
        print('Hãy nhập lại')
