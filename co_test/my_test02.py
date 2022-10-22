# print("*****")
# print("*   *")
# print("*   *")
# print("*   *")
# print("*****")

# for i in range(5):
#     if i == 0 or i == 4:
#         print("*****")
#     else:
#         print("*   *")

my_list = range(5)
for i in my_list:
    if i == 0 or i == len(my_list) - 1:
        print("*****")
    else:
        print("*   *")
