#   

# a = [1, 3, 4, 9, 8, 6, ]
# for i in a.copy():
#     if i % 2 == 0:
#         a.remove(i)
#         print(a)



# task_1


# a = input("tell me your name \n")
# a = a.split()
# print(a[::-1])







# task_2
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# c = []
# c.extend(a)
# c.extend(b)
# for i in c:
#     if c.count(i) > 1:
#         c.remove(i)
#         c.sort()

#         print(c)


# task_3


# dict_1 = {1: 10, 2: 20}
# dict_2 = {3: 30, 4: 40}
# dict_3 = {5: 50, 6: 60}
# dict_4 = {6: 50, 7: 60}
# list_dict = [dict_1, dict_2, dict_3, dict_4]
# n = {}
# for i in list_dict:
#     n.update(i)
# print(n)


# task_4

# org_dict = {"c1": "red", "c2": "green", "c3": None, "c4": None}
# for key, value in org_dict.copy().items():
#     if value is None:
#         org_dict.pop(key)
#         print(org_dict)


# task_5

# a = {}
# b = []
# for i in range(1,6):
#     b.append(i)
#     b.append(i*i)
#     print(b)
#     for i in b:
#         a[i] = i
#         print(a)