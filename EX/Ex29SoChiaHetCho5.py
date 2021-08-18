
a = int(input('Enter a:'))
b = int(input('Enter b: '))
if a > b:
    print('a must be smaller than')
else:
    count = 0
    for i in range(a, b + 1):
        if i % 5 == 0:
            print(i)
            count += 1
            if(count > 10):
                break
