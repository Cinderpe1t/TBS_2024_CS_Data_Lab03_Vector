# 2024 CS Algorithm and Data Structure Lab #3 - Vector Class
Define a class for 3D vector mathematics, and apply unit test
## Python codes
- `vector.py`: `Vector3D` class definition
- `my_vector.py`: Demostrate `Vector3D` class operations
- `test_vector.py` : Unit test `Vector3D` class
- `$ python3 my_vector.py` executes the demonstration
- `$ python3 test_vector.py` executes the unit test
## Operations
- `+`, `Vector3D.add()`: 3D vector addition
- `-`, `Vector3D.subtract()`: 3D vector subtraction
- `*`, `Vector3D.scalar_product()`: 3D vector scale a vector
- `*`, `Vector3D.dot_product()`: 3D vector dot product
- `abs()`, `Vector3D.length()`: 3D vector length
- `Vector3D.cos()`: cosine of two vectors
- `Vector3D.sin()`: sine of two vectors
- `Vector3D.tan()`: tangent of two vectors
- `Vector3D.acos()`: angle in degree of two vectors from cosine
- `Vector3D.is_perpendicular()`: check if two vectors are perpendicular
- `**`, `Vector3D.cross_product()`: cross product of two vectors
- `==`, `!=`: vector comparison
## Output of my_test.py
```
------------------------------
Vector case 1
------------------------------
Vector a:  Vector <1,0,2>
Vector b:  Vector <0,1,-1>
Vector a:  Vector3D(1,0,2)
Vector b:  Vector3D(0,1,-1)
Vector a:  Vector <1,0,2>
Vector b:  Vector <0,1,-1>
------------------------------
a.add(b):  Vector <1,1,1>
a + b:  Vector <1,1,1>
a.subtract(b):  Vector <1,-1,3>
a - b:  Vector <1,-1,3>
a * 3:  Vector <3,0,6>
a.scalar_product(3):  Vector <3,0,6>
a * b:  -2
a.dot_product(b):  -2
abs(a):  2.23606797749979
a.length():  2.23606797749979
a.cos(b):  -0.6324555320336759
a.sin(b):  0.7745966692414833
a.tan(b):  -1.224744871391589
a.acos(b):  129.23152048359225
a.is_perpendicular(b):  False
a ** b:  Vector <-2,1,1>
a.cross_product(b):  Vector <-2,1,1>
a == b:  False
a == a:  True
a != b:  True
a != a:  False
------------------------------
Vector case 2
------------------------------
Vector a:  Vector <1,0,0>
Vector b:  Vector <0,1,0>
------------------------------
a * b:  0
a.dot_product(b):  0
a.cos(b):  0.0
a.sin(b):  1.0
a.acos(b):  90.0
a.is_perpendicular(b):  True
a ** b  Vector <0,0,1>
a.cross_product(b):  Vector <0,0,1>
```

## Output of test_vector.py (assuming all goes well)
```
..............
----------------------------------------------------------------------
Ran 14 tests in 0.001s

OK
```
