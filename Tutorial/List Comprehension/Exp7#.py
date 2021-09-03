# transactions = [100, 200, 300, 150, 80]
# TAX_RATE = 0.08
# SERVICE_CHARGE = 0.07


# def get_price_tax_service(bill):
#     return bill*(1 + TAX_RATE + SERVICE_CHARGE)


# final_price = [get_price_tax_service(bill) for bill in transactions]
# print(get_price_tax_service(100))  # in 1 hoa don
# print(final_price) # tat ca hoa don

# Advanced Functions
# list()-->convert strings => list
# my_strings = "welcome to my world"
# list_of_charts = list(my_strings)
# print(list_of_charts)

# --------------------------------------------
# zip(): looping through two list simultaneously
# wizards = ['Harry potter', 'Ron', 'Hermione']

# pets = ['Hedwig', 'Scabber', 'Crookshank']
# # enumerate nang cao
# for index, (wiz, pet) in enumerate(zip(wizards, pets)):
#     print(f'{index + 1}. {wiz} has {pet}')
# sorted()
# TH1
# sorted_by_first = sorted(['hi', 'hello', 'you', 'char', 'youtube', 'anne'])
# print(sorted_by_first)  # sort by bang chu cai dau tien
# -----------------------------------------------------------
# TH2
# sorted_by_second = sorted(
#     ['hi', 'hello', 'you', 'char', 'haha', 'youtube', 'anne'], key=lambda x: x[1])  # index 1
# print(sorted_by_second)
# -----------------------------------------------------------
# TH3
# sorted_by_key = sorted([
#                        {'name': 'Bina', 'age': 30},
#                        {'name': 'Andy', 'age': 18},
#                        {'name': 'zoey', 'age': 55}],
#                        key=lambda el: (el['name']))
# print(sorted_by_key)
# -----------------------------------------------------------
'''
5. 2D Array/List = Matrix: Mảng 2 Chiều
'''

# Matrix   0  1  2
matrix = [[1, 2, 3],    # 0
          [4, 5, 6],    # 1
          [7, 8, 9]]    # 2
# print(matrix[1][2])     # => 6
# Transform matrix in list format
# list_converted = [matrix[row][column]
#                   for row in range(len(matrix)) for column in range(len(matrix))]
# print(list_converted)
# => [1, 2, 3, 4, 5, 6, 7, 8, 9]
# With Zip
print([x for x in zip(*matrix)])  # => [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
