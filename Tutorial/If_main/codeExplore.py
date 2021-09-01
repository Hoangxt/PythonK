# sub module
#print(f"sub_module 's name {__name__}")

def welcome():
    print("Welcome to Python")


def fun1():
    print("This is fun1 function")


def main():
    welcome()
    fun1()

# main function will run
# khi import vào những file khác thì sẽ ko chậy tất cả hàm có trong main
if __name__ == "__main__":
    main()
