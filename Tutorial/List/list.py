
'''
list : List trong python - một dạng dữ liệu  cho phép  lưu trữ nhiều kiểu dữ liệu khác  nhau trong trong nó
và chúng ta có thể truy xuất đến các phần tử bên trong nó thông qua vị trí của phần tử đó trong list

Ngôn ngữ khác: C/C++, Java, List trong Python = Mảng (Array)

'''
# 1.Creating list
# list1 = ['banana', 'apple', 'orange', 'cherry']
# list2 = [4, 'Hoang', False, None]
# list3 = list()  # empty list
# print(list1)
# print(list2)
# print(list3)
# --------------------------------------------------------------------------------------
# 2.Access elements: Truy cập đến các giá trị trong list
# my_list = [1, 2, '3', 5, 5, 5, '5', True]
# print(len(my_list))  # length list
# print(my_list[2])  # index 2 = 3 (start from 0)
# print(my_list.index('3'))  # find position
# print(my_list.count(5))  # 3 number 5 , 1 '5'

# print all
# for item in my_list:
#     print(item)
# Python's built-in enumerate function

# presidents = ['Washington', 'Adams',
#               'Jefferson', 'Madison', 'Monroe', 'Jackson']
# print(presidents)
# # start from index 1 (#1,....)
# for index, president in enumerate(presidents, start=1):
#     print(f"President #{index}: {president}")
# ----------------------------------------------------------------------------------------
# Slicing (Cắt)
# : is called slicing and
# has the format [start : end : step]
# myList = [1, 2, '3', True, False]
# print(myList[1:])  # print from index 1 to end,
# print(myList[-1])  # [-1] vị trí cuối cùng của list
# print(myList[::-1])  # reversed string
# ----------------------------------------------------------------------------------------
# 3. List Operations & Useful Method
# 3.1 Add to list
# myList = [1, 2, '3', True, False]
# print(myList*2)
# print(myList + [100, 'new index'])
# ---------------------------------------------------------------------------------------
# print(myList.append(100)) # add 1 value,
# print(myList.extend([6, 9, 'add more']))  # extend add more than 1
# insert add tại ví trí nào đó
# myList.insert(3,4)
# print(myList)
# ---------------------------------------------------------------------------------------
# Remove from list
# myList = [1, 2, '3', True, 2, 2]
# # delete last
# # myList.pop()
# myList.remove(2)  # remove first occurrence of item or raises ValueError
# # myList.reverse()
# print(myList)
# ----------------------------------------------------------------------------------------
# 3.3 Sorting
# myList = [1, 5, 3, 7, 4, 8, 53, 3]
# myList.sort()  # tang dan
# myList.sort(reverse=True)  # giam dan
# print(sorted(myList))
# print(myList)
# ----------------------------------------------------------------------------------------
# 3.4Useful Method
# myList = [1, 5, 3, 7, 4, 8, 53, 3]
# print(max(myList))
# print(min(myList))
# print(sum(myList))
