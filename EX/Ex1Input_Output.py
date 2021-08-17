# có xử lý ngoại lệ đầu vào
# try:
#     print("Enter first number: ")
#     so1 = int(input())
#     print("Enter second number: ")
#     so2 = int(input())
#     sum = so1 + so2
#     print("sum:", sum)
# except:
#     print("Error")
while True:
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        sum = a+b
        print("Sum:", sum)
        break
    except:
        print("Error!!! Re Enter :v")
