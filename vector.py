"""
Name: Angelina Kim
Date: Fall 2024
Purpose: Implement 3D vector mathematics class
"""
import math
from typing import Union
from typing import Any, Self

class Vector3D:
    """3D vector calculation class"""
    def __init__(self, x: float = 0, y: float = 0, z: float = 0):
        self.x = x
        self.y = y
        self.z = z
    
    def __str__(self) -> str:
        return "(%s, %s, %s)" % (self.x, self.y, self.z)

    def __repr__(self) -> str:
        return "(%s, %s, %s)" % (self.x, self.y, self.z)

    def add(self, other: Self) -> Self:
        """Add self and other 3D vectors."""
        return self.__class__(self.x + other.x, self.y + other.y, 
                              self.z + other.z)
    
    def __add__(self, other: Self) -> Self:
        """Add two 3D vectors."""
        return self.__class__(self.x + other.x, self.y + other.y, 
                              self.z + other.z)
    
    def sub(self, other: Self) -> Self:
        """Subtract self and other 3D vectors."""
        return self.__class__(self.x - other.x, self.y - other.y, 
                              self.z - other.z)
    
    def __sub__(self, other: Self) -> Self:
        """Subtract two 3D vectors."""
        return self.__class__(self.x - other.x, self.y - other.y, 
                              self.z - other.z)

    def dot_product(self, other: Self) -> float:
        """Dot or inner product of two vectors."""
        inner_product = self.x * other.x + self.y * other.y + self.z * other.z
        return inner_product

    def __mul__(self, other: Self) -> Union[float, Self, None]:
        """Dot or inner product of two vectors or scale a vector."""
        if isinstance(other, Vector3D):
            inner_product = self.dot_product(other)
            return inner_product
        elif isinstance(other, (int, float, complex)):
            x, y, z = other * self.x, other * self.y, other * self.z
            return self.__class__(x, y, z)
        else:
            return None

    def __rmul__(self, other: Self) -> Self:
        """Scale a vector."""
        return self * other # call __mul__
    
    def scalar_product(self, scale: float) -> Self:
        """Scalar product of a vector."""
        return self * scale # call __mul__
    
    def __abs__(self) -> float:
        """Length of a vector."""
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)

    def length(self) -> float:
        """Length of a vector using abs."""
        return abs(self)

    def cos(self, other: Self) -> float:
        """Obtain cosine value using inner product."""
        return self * other / ( self.length() * other.length() ) # call __mul__

    def sin(self, other: Self) -> float:
        """Obtain sine value using outer product."""
        cross = self.cross_product(other)
        return cross.length() / ( self.length() * other.length() )

    def tan(self, other: Self) -> float:
        """Obtain tangent value using outer product."""
        return self.sin(other) / self.cos(other)

    def acos(self, other: Self) -> float:
        """Obtain arc-cosine angle of the two vectors."""
        return math.acos( self.cos(other) ) * 180 / math.pi
        
    def is_perpendicular(self, other: Self) -> bool:
        """Check if two vectors are perpendicular."""
        if self * other == 0:
            return True
        else:
            return False

    def __pow__(self, other: Self) -> Self:
        """Use ** to return 3D vector's cross product."""
        cross_x = self.y * other.z - self.z * other.y
        cross_y = self.z * other.x - self.x * other.z
        cross_z = self.x * other.y - self.y * other.x
        return self.__class__(cross_x, cross_y, cross_z)

    def cross_product(self, other: Self) -> Self:
        """Return 3D vector's cross product using **."""
        return self ** other

    def __eq__(self, other: Self) -> bool:
        """Compare vectors."""
        if self.x == other.x and self.y == other.y and self.z == other.z:
            return True
        else:
            return False

    def __ne__(self, other: Self) -> bool:
        """Compare vectors - not equal."""
        return not (self == other)
