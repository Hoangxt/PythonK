
my_dict = {"name": "Hoang", "age": 21, "city": "New York", "content": "Noob"}
print(my_dict)

# my_dict_2 = dict(name="HoangDZ", content="Noob1no2", city="Nam Dinh")

# print(my_dict_2)
# Access items
# content_in_dict = my_dict["content"]
# print(content_in_dict)
# ----------------------------------------------------------------
# check for keys in my_ C1
# if "name" in my_dict:
#     print(my_dict["name"])
# else:
#     print("No key found")
# ----------------------------
# C2
# try:
#     print(my_dict["age"])
# except KeyError:
#     print("No key found")
# Add new key
# my_dict["email"] = "test@xyz.com"
# print(my_dict)

# or overwrite the now existing key
my_dict["email"] = "change@xyz.com"
print(my_dict)
# Delete items
# delete a key-value pair
del my_dict["email"]
