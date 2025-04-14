#isintance - проверяет принадлежит ли классу
#  class Soda:
#     def __init__(self, ingridient):
#         if isinstance(ingridient,str):
#             self.ingridient = ingridient
#         else:
#             self.ingridient = None
#     def show_my_drink(self):
#         if self.ingridient:
#             print(f"Газировка и {self.ingridient}")
#         else:
#             print("Обычная газировка")
# drink1 = Soda("малина")
# drink2 = Soda(3)
# drink1.show_my_drink()
# drink2.show_my_drink()


#Требуется проверить, возможно ли из представленных отрезков условной длины сформировать 
# треугольник. Нужно создать класс TriangleChecker, 
# прнимающий в себя только положительные числа. С помошью метода is_tringle() возвращаются 
# следюущие значения (в зависимости от ситуации):
# - Ура, можно построить треугольник;
# - С отрицальными числами ничего не выйдет
# - Нужно вводить только числа!;
# - Жаль, но из этого не получтся треугольник.
# class TriangleChecker:
#     def __init__(self, sides):
#         self.sides = sides
#
#     def is_triangle(self):
#         if all(isinstance(side,(int,float))for side in self.sides):
#             if all(side>0 for side in self.sides):
#                 sorted_sides = sorted(self.sides)
#                 if sorted_sides[0]+sorted_sides[1]>sorted_sides[2]:
#                     return "Ура, из этого можно построить треугольник"
#                 return "Жаль, но из этого не получится треугольник"
#             return "С отрицательными числами, ничего не выйдет"
#         return "Нужно вводить только числа!"

# triangle1 = TriangleChecker([2,3,4])
# print(triangle1.is_triangle())
# triangle2 = TriangleChecker([-2,3,4])
# print(triangle2.is_triangle())
# triangle3 = TriangleChecker([2,3,"Side3"])
# print(triangle3.is_triangle())

#Николай
# class Nikola:
#     def __init__(self, name, age):
#         if name == "Николай":
#            self.name = name
#         else:
#             self.name = f"Я не {name}, а Николай"
#         self.age = age
# user1 = Nikola("Никита",12)
# print(user1.name)

