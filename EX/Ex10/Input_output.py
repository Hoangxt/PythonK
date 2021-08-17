# Mo file voi mode='r' de doc file
try:
    with open('input.txt', 'r', encoding='utf-8') as fileInp:
        name = fileInp.readline().rstrip('\n')
        age = int(fileInp.readline())
    with open('output.txt', 'w', encoding='utf-8') as fileOut:
        fileOut.write('30 năm nữa, tuổi của {} sẽ là {}'.format(
            name, age + 30))
        print('đã tạo ra file output Thành Công')
except FileNotFoundError:
    print('file không tồn tại')
except:
    with open('output.out', 'w', encoding='utf-8') as fileOut:
        print('dữ liệu không hợp lệ')
