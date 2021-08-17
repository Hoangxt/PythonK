try:
    with open('input.txt', 'r', encoding='utf-8') as fileInp:
        data = fileInp.readlines()
        StringJoind = ' '.join(data).replace('\n', '')

        list = StringJoind.split()
        StringJoind = ' '.join(list)

        print(StringJoind)
    fileOut = open('output.txt', 'wb')
    fileOut.write(StringJoind.encode('utf-8'))
except:
    print('Lỗi đọc/ghi file')
