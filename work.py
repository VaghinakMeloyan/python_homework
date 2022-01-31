# Task_1
class Triangle:
    def __init__(self, first, second, third, *args):
        super().__init__(*args)
        self.first = first
        self.second = second
        self.third = third

    def perimeter(self):
        return self.first + self.second + self.third

    def semi_perimeter(self):
        return self.perimeter() / 2

    def area(self):
        return  0.5 *  self.semi_perimeter() * (self.semi_perimeter() - self.first) * \
         (self.semi_perimeter() - self.second) * \
                (self.semi_perimeter() - self.third)


    def sorted(self):
        # if not isinstance(self.first(int, float)) and isinstance(self.second(int, float)) and isinstance(self.third(int, float)):
        #     raise TypeError
        return sorted((self.first, self.second, self.third))

    def is_alike(self, other):
        if type(other) is not Triangle:
            raise TypeError
        sorted_list_1 = self.sorted()
        sorted_list_2 = other.sorted()
        return sorted_list_1[0] / sorted_list_2[0] == sorted_list_1[1] / sorted_list_2[1] == sorted_list_1[2] / \
               sorted_list_2[2]



object_1 = Triangle(2, 5, 4)
object_2 = Triangle(8, 10, 4)


print(object_1.perimeter())
print(object_1.semi_perimeter())
print(object_1.area())
print(object_1.is_alike(object_2))

# Task_2

class Rectangular:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth

    def sorted(self):
        return sorted((self.first, self.second, self.third, self.fourth))

    def Rectangular_contains(self, other):
        if type(other) is Rectangular:
            first_list = self.sorted()
            second_list = other.sorted()
            if first_list[0] > second_list[0] and first_list[1] > second_list[1] and \
                first_list[2] > second_list[2] and first_list[3] > second_list[3]:
                return "rectangulator_2 is contain in rectangulator_1"
            else:
                return " rectangulator_2 is not contains in rectangulator_1"
object_1 = Rectangular(2, 2, 4, 4)
object_2 = Rectangular(4, 4, 8, 8)

print(object_1.Rectangular_contains(object_2))
