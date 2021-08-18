# ve tam giac
n = int(input('Enter n:'))
if n < 1 or n > 9:
    print('n must between 1 and 9')
else:
    for i in range(1, n + 1):
        line = ""
        for j in range(1, i + 1):
            line = "{} {}".format(line, j)
        print(line)
