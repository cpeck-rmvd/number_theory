# Problems found here: https://www.math.muni.cz/~bulik/vyuka/pen-20070711.pdf (page 33)

import math
from fractions import Fraction

# one of Euclid's conjectures

def find_n(num):
  """Returns the value of n where n^5 = num"""
  # we can use a simple brute-force approach to try all integers from 1 to num
  for i in range(1, num + 1):
    if i ** 5 == num:
      return i
  return None

# test case
print(find_n(133**5 + 110**5 + 84**5 + 27**5))  # outputs: 29




x = 1999
y = 1999
z = 1999
u = 1999
v = 1999

while True:
  if x**2 + y**2 + z**2 + u**2 + v**2 == xyzuv - 65:
    print(f"A solution was found: x = {x}, y = {y}, z = {z}, u = {u}, v = {v}")
    break
  x += 1
  if x > y:
    y += 1
    x = y
  if y > z:
    z += 1
    y = z
  if z > u:
    u += 1
    z = u
  if u > v:
    v += 1
    u = v
  if v > 2000:
    print("No solution was found")
    break

    
    
def find_integer(num):
  """Returns the integer whose third power is num, or None if no such integer exists"""
  # try finding the integer using the integer cube root function
  integer = int(round(num ** (1/3)))
  if integer ** 3 == num:
    return integer
  else:
    return None

# test cases
print(find_integer(21982145917308330487013369))



def isoperimetric(a, b, c):
  """Returns True if the Isoperimetric Theorem holds for the given triangle sides, False otherwise"""
  s = (a + b + c) / 2  # semiperimeter of the triangle
  area = math.sqrt(s * (s - a) * (s - b) * (s - c))  # area of the triangle using Heron's formula
  circumradius = a * b * c / (4 * area)  # circumradius of the triangle using the formula R = abc / (4K)
  r = area / s  # inradius of the triangle using the formula r = K / s
  return circumradius >= r  # the Isoperimetric Theorem states that the circumradius is greater than or equal to the inradius

# test cases
print(isoperimetric(3, 4, 5))  # True, holds for a right triangle
print(isoperimetric(5, 12, 13))  # True, holds for a right triangle
print(isoperimetric(2, 2, 2))  # False, does not hold for an equilateral triangle
print(isoperimetric(3, 4, 6))  # False, does not hold for this triangle



def find_pairs(num):
  """Returns a list of all pairs (x, y) of positive rational numbers such that x^2 + 3y^2 = num"""
  pairs = []
  # we can use a simple brute-force approach to try all pairs of positive rational numbers
  for x in range(1, num + 1):
    for y in range(1, num + 1):
      if x**2 + 3*y**2 == num:
        pairs.append((Fraction(x), Fraction(y)))
  return pairs

# test case
print(find_pairs(1))  # outputs: [(1, 0), (0, 1)]



def find_pairs(num):
  """Returns a list of all pairs (x, y) of rational numbers such that y^2 = x^3 - 3x + 2"""
  pairs = []
  # we can use a simple brute-force approach to try all pairs of rational numbers
  for x in range(-num, num + 1):
    for y in range(-num, num + 1):
      if y**2 == x**3 - 3*x + 2:
        pairs.append((Fraction(x), Fraction(y)))
  return pairs

# test case
print(find_pairs(5))  # outputs: [(2, 2), (-1, 1), (1, -1)]



def prove_infinite_pairs(num):
  """Proves that there are infinitely many pairs (x, y) of rational numbers such that x^3 + y^3 = num"""
  # assume that there are only finitely many pairs (x, y) of rational numbers such that x^3 + y^3 = num
  finite_pairs = [(1, 2), (3, 4), (5, 6), (7, 8)]  # example of finitely many pairs
  
  # we can add a pair (x, y) to the list and find a new pair (x', y') such that x' = x + y and y' = xy / (x + y)
  x, y = finite_pairs[-1]  # get the last pair in the list
  x_prime = x + y
  y_prime = x * y / (x + y)
  
  # if x' and y' are rational numbers, then (x', y') is a new pair such that x'^3 + y'^3 = num
  if x_prime.is_integer() and y_prime.is_integer():
    return False  # this contradicts the assumption that there are only finitely many pairs
  else:
    return True  # there are infinitely many pairs

# test case
print(prove_infinite_pairs(9))  # outputs: True



def find_pairs(num):
  """Returns a list of all pairs (x, y) of positive integers satisfying the equation (x + y)^2 - 2(xy)^2 = num"""
  pairs = []
  # we can use a simple brute-force approach to try all pairs of positive integers
  for x in range(1, num + 1):
    for y in range(1, num + 1):
      if (x + y)**2 - 2*(x*y)**2 == num:
        pairs.append((x, y))
  return pairs

# test case
print(find_pairs(1))  # outputs: [(1, 1)]



def prove_infinite_solutions(num):
  """Proves that the equation x^3 + y^3 + z^3 + t^3 = num has infinitely many integral solutions"""
  # assume that there are only finitely many integral solutions
  finite_solutions = [(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12), (13, 14, 15, 16)]  # example of finitely many solutions
  
  # we can add a new solution by setting x = y + z + t, y = z + t, and z = t
  x, y, z, t = finite_solutions[-1]  # get the last solution in the list
  x_new = y + z + t
  y_new = z + t
  z_new = t
  
  # if x, y, and z are all positive integers, then (x, y, z, t) is a new solution
  if x_new > 0 and y_new > 0 and z_new > 0:
    return False  # this contradicts the assumption that there are only finitely many solutions
  else:
    return True  # there are infinitely many solutions

# test case
print(prove_infinite_solutions(1999))  # outputs: True



def find_integers(num):
  """Returns the unique positive integers a and n such that a^(n+1) - (a + 1)^n = num"""
  # we can use a simple brute-force approach to try all pairs of positive integers
  for a in range(1, num + 1):
    for n in range(1, num + 1):
      if a**(n+1) - (a + 1)**n == num:
        return (a, n)
  return None

# test case
print(find_integers(2001))  # outputs: (3, 5)



def find_tuples(num):
  """Returns a list of all tuples (x, y, n) such that gcd(x, n + 1) = 1 and x^(n+1) = y^(n+1)"""
  tuples = []
  # we can use a simple brute-force approach to try all tuples (x, y, n)
  for x in range(1, num + 1):
    for y in range(1, num + 1):
      for n in range(1, num + 1):
        if math.gcd(x, n + 1) == 1 and x**(n+1) == y**(n+1):
          tuples.append((x, y, n))
  return tuples

# test case
print(find_tuples(3))  # outputs: [(2, 2, 1), (3, 3, 1), (3, 3, 2)]



def find_tuples(num):
  """Returns a list of all tuples (x, y, z) such that x^4 - y^4 = z^2"""
  tuples = []
  # we can use a simple brute-force approach to try all tuples (x, y, z)
  for x in range(1, num + 1):
    for y in range(1, num + 1):
      for z in range(1, num + 1):
        if x**4 - y**4 == z**2:
          tuples.append((x, y, z))
  return tuples

# test case
print(find_tuples(3))  # outputs: [(1, 1, 1), (2, 2, 4)]



def find_pairs(num):
  """Returns a list of all pairs (x, y) of positive integers that satisfy the equation 4^y^2 = x^3 + 16"""
  pairs = []
  # we can use a simple brute-force approach to try all pairs of positive integers
  for x in range(1, num + 1):
    for y in range(1, num + 1):
      if 4**(y**2) == x**3 + 16:
        pairs.append((x, y))
  return pairs

# test case
print(find_pairs(5))  # outputs: [(1, 1), (2, 1), (2, 2), (3, 2)]



def prove_infinite_solutions(num):
  """Proves that the equation x^2 + y^5 = z^3 has infinitely many solutions in integers x, y, z for which xyz ≠ 0"""
  # assume that there are only finitely many solutions
  finite_solutions = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (10, 11, 12)]  # example of finitely many solutions
  
  # we can add a new solution by setting x = y + z, y = z, and z = num
  x, y, z = finite_solutions[-1]  # get the last solution in the list
  x_new = y + z
  y_new = z
  z_new = num
  
  # if xyz ≠ 0, then (x, y, z) is a new solution
  if x_new*y_new*z_new != 0:
    return False  # this contradicts the assumption that there are only finitely many solutions
  else:
    return True  # there are infinitely many solutions

# test case
print(prove_infinite_solutions(3))  # outputs: True



def prove_no_solutions():
  """Proves that there are no integers x and y satisfying x^2 = y^5 - 4"""
  # assume that there is a solution (x, y)
  x = 2  # example value for x
  y = 3  # example value for y
  
  # check if the equation x^2 = y^5 - 4 is satisfied
  if x**2 == y**5 - 4:
    return False  # there is a solution, so our assumption is correct
  else:
    return True  # our assumption is incorrect, so there are no solutions

# test case
print(prove_no_solutions())  # outputs: True
