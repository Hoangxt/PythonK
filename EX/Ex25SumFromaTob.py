try:
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))

    if a > b:
        print('a must < b')
    else:
        sum = 0
        for i in range(a, b+1):
            sum += i
        print("Sum: {}".format(sum))
except:
    print("Error!")
