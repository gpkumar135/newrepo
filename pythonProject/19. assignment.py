'''class A:
    def __init__(self,a):
        self.a = a

    def __add__(self,o):
        return self.a + o.a
obj1 = A(1)
obj2 = A(2)
obj3 = A("pk")
obj4 = A("gpk")

print(obj1 + obj2)
print(obj3 + obj4)
  ## binary operator is used to print
print(A.__add__(obj1 , obj2))
print(A.__add__(obj3 , obj4))'''


     #duck typing#
     #Duck Typing is a type system used in dynamic languages. For example, Python, Perl, Ruby, PHP, Javascript, etc. where the type or the class of an object is less important than the method it defines. Using Duck Typing, we do not check types at all. Instead, we check for the presence of a given method or attribute.
# class Bird:
#     def fly(self):
#         print("fly with wings")
#
# class Airplane:
#     def fly(self):
#         print("fly with fuel")
#
# class Fish:
#     def swim(self):
#         print("fish swim in sea")
#
#     # Attributes having same name are
#
# # considered as duck typing
# for obj in Bird(), Airplane(), Fish():
#     obj.fly()

# shallow copy
# import copy
#
# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.copy(old_list)
#
# new_list[1][1] = 'pk'
#
# print("Old list:", old_list)
# print("New list:", new_list)

# deep copy

#import copy

# old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
# new_list = copy.deepcopy(old_list)
# new_list[0][1] = 'AB'
# print("Old list:", old_list)
# print("New list:", new_list)


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def __str__(self):
#         return f"({self.x}, {self.y})"
#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"
#
# a = Point(1,3)
# print(a)


# class Employee:
#     def __init__(self,string):
#         self.string = string
#     def __getitem__(self, item):
#         return
#     def __setitem__(self, key, value):
#         self.string[key] = value
#
# e = Employee({1:"2",3:"4",5:"6"})
# print(e.string)
# e[1] = '5'
# print(e[1])

