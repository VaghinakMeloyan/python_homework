# Task_1

# class Circle:
#     def __init__(self, radius):
#         if not isinstance(radius, (int, float)):
#             raise TypeError
#         self.radius = radius

#     def area(self):
#         return self.radius ** 2 * 3.14

#     def parimeter(self):
#         return self.radius * 2 * 3.14

# object_1 = Circle(5)

# print(object_1.area())
# print(object_1.parimeter())


# Task_2

# class Human:
#     import datetime
#     yer = datetime.datetime.today()
#     yer = yer.year

#     def __init__(self, name, surname, age, height, weight):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.height = height
#         self.weight = weight

#     def present(self):
#         return self.name, self.surname, self.age, self.height, self.weight

#     def optimal_weight(self):
#         return self.height - 100

#     def will_be_100(self):
#         return f"{self.yer - self.age + 100} you will be 100 "

# object_1 = Human("Vaghinak", "Meloyan", 29, 177, 70)
# print(object_1.present())
# print(object_1.optimal_weight())
# print(object_1.will_be_100())
