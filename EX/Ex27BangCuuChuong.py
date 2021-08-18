try:
    n = int(input('Enter n: '))
    if n < 1 or n > 9:
        print('n must be between 1 and 9')
    else:
        for i in range(1, 11):
            print('{} * {} = {}'.format(n, i, n*i))  # ez qua :))
except:
    print('Error')
