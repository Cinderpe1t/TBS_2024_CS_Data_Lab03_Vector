"""
Name: Angelina Kim
Date: Fall 2024
Purpose: Demonstrate Vector3D class and operations.
"""

from vector import Vector3D

# Vector case #1
a = Vector3D(1, 0, 2)
b = Vector3D(0, 1, -1)

print("------------------------------")
print("Vector case 1")
print("------------------------------")
print("Vector a: ", a)
print("Vector b: ", b)
print("Vector a: ", repr(a))
print("Vector b: ", repr(b))
print("Vector a: ", eval(repr(a)))
print("Vector b: ", eval(repr(b)))


print("------------------------------")
print("a.add(b): ", a.add(b))
print("a + b: ", a + b) # __add__
print("a.subtract(b): ", a.subtract(b))
print("a - b: ", a - b) # __subtract__
print("a * 3: ", a * 3) # __mul__
print("a.scalar_product(3): ", a.scalar_product(3))
print("a * b: ", a * b) # __mul__
print("a.dot_product(b): ", a.dot_product(b))
print("abs(a): ", abs(a))
print("a.length(): ", a.length())
print("a.cos(b): ", a.cos(b))
print("a.sin(b): ", a.sin(b))
print("a.tan(b): ", a.tan(b))
print("a.acos(b): ", a.acos(b))
print("a.is_perpendicular(b): ", a.is_perpendicular(b))
print("a ** b: ", a ** b) # __pow__
print("a.cross_product(b): ", a.cross_product(b))
print("a == b: ", a == b)
print("a == a: ", a == a)
print("a != b: ", a != b)
print("a != a: ", a != a)

# Vector case #2
a = Vector3D(1, 0, 0)
b = Vector3D(0, 1, 0)
print("------------------------------")
print("Vector case 2")
print("------------------------------")
print("Vector a: ", a)
print("Vector b: ", b)
print("------------------------------")
print("a * b: ", a * b) # __mul__
print("a.dot_product(b): ", a.dot_product(b))
print("a.cos(b): ", a.cos(b))
print("a.sin(b): ", a.sin(b))
print("a.acos(b): ", a.acos(b))
print("a.is_perpendicular(b): ", a.is_perpendicular(b))
print("a ** b ", a ** b) # __pow__
print("a.cross_product(b): ", a.cross_product(b))