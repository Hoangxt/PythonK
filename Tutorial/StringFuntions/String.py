# String str
# Mutable (can be changed): list, dict, set, bytearray
# Immutable (can not be changed): int , float, decimal, boolean,bytes

# Escaping Backslash \
# my_string = 'Hello i\'m a "men" '
# print(my_string)

# Access characters and substrings

# my_string = "Hello World"
#            012345678910
# get character by referring to index
# char = my_string[0]
# print(char)
# Substrings with slicing
# StringName [startIndex:endIndex]
# start at index 1 and go until index 5 (not include 5)
# sub_string1 = my_string[1:5]
# sub_string0 = my_string[:5]
# sub_stringEnd = my_string[5:]

# revere_string = my_string[::-1]
# print(sub_string1)
# print(sub_string0)
# print(sub_stringEnd)
# print(revere_string)

'''
Concatenate two or more strings
'''
# concat string with +
# greeting = "Hello,xin chao cac ban"
# channel = "Learn python"
# sentence = greeting + "chao mung cac ban den voi channel cua " + channel
# print(sentence)

# join element of a list into a string:
# my_list = ['How', 'are', 'you', 'today']
# sentencJoin = '*'.join(my_list)
# print(sentencJoin)

# Tiếp cận từng kí tự một trong vòng lặp

# my_string = "Hello xin chao cac ban"

# for character in my_string:
#     print(character)
# if "x" in my_string:
#     print("yes")
# else:
#     print("no")


'''
Hàm cơ bản và hữu ích
'''

# strip() - > Xóa Tất cả khoảng trắng từ đầu đến cuối
# print("  i am alone    ".strip())
# print("at home".strip('o'))  # => xoa o

# split() Tách chỗi
# print('life is good'.split())
# print('but, it very boring'.split(','))

# replace thay the mot so tu trong string
# startwith
# find
# title chi in hoa chu dau tien cua moi tu trong choi
# capitalize in hoa chu cai dau tien trong choi
# count

# string formatting
# %,.format(),f-string
name = "hello new world"
my_string1 = "welcome to %s" % name
print(my_string1)

pi = 3.1415926535
s = "pi number"
my_string = "variable is %f from %s" % (pi, s)
print(my_string)

# .format
age = 24
my_age = "i am {} year old ".format(age)
print(my_age)
