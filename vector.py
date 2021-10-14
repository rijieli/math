from typing import List

Vector = List[float]

def scale(scalar: float, vector: Vector) -> Vector:
	return [scalar * num for num in vector]

def plus(lhs: Vector, rhs: Vector) -> Vector:
	# validate size
	if len(lhs) != len(rhs):
		raise TypeError("Vector not in same dimension")

	

	return list(map(add, lhs, rhs))

def add(lhs: float, rhs: float) -> float:
	return lhs + rhs


v1 = [2, 9 ,4]
v2 = [3, 8 ,11]
v1o = [2, 9, 4, 12]

print(scale(2.5, v1))

print(plus(v1, v1o))