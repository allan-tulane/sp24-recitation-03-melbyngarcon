"""
CMPS 2200  Recitation 3.
See recitation-03.md for details.
"""
import time

class BinaryNumber:
    """ done """
    def __init__(self, n):
        self.decimal_val = n               
        self.binary_vec = list('{0:b}'.format(n)) 
        
    def __repr__(self):
        return('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))
    

## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def add_binary_numbers(a, b):
  # Convert binary vectors to integers, add them, and convert back to BinaryNumber
  sum_decimal = a.decimal_val + b.decimal_val
  return BinaryNumber(sum_decimal)
  
def binary2int(binary_vec): 
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))

def split_number(vec):
    return (binary2int(vec[:len(vec)//2]),
            binary2int(vec[len(vec)//2:]))

def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)
    
def pad(x, y):
    # Extract binary vectors from BinaryNumber objects
  x_vec, y_vec = x.binary_vec, y.binary_vec

    # Pad with leading 0s if x_vec and y_vec have different lengths
  if len(x_vec) < len(y_vec):
    x_vec = ['0'] * (len(y_vec) - len(x_vec)) + x_vec
  elif len(y_vec) < len(x_vec):
    y_vec = ['0'] * (len(x_vec) - len(y_vec)) + y_vec

    # Pad with a leading 0 if the number of bits is not even
  if len(x_vec) % 2 != 0:
    x_vec = ['0'] + x_vec
    y_vec = ['0'] + y_vec

    # Return the padded vectors as BinaryNumber objects
  return binary2int(x_vec), binary2int(y_vec)

def quadratic_multiply(x, y):
    # this just converts the result from a BinaryNumber to a regular int
    return _quadratic_multiply(x,y).decimal_val

def _quadratic_multiply(x, y):
    # Pad x and y to ensure they have the same length and are even-length
  x, y = pad(x, y)

    # Calculate the number of bits
  n = len(x.binary_vec)

    # Base case: If the length of the binary vectors is 1
  if n == 1:
    return BinaryNumber(x.decimal_val * y.decimal_val)

    # Divide: Split x and y into left and right halves
  x_left, x_right = split_number(x.binary_vec)
  y_left, y_right = split_number(y.binary_vec)

    # Conquer: Recursively calculate the products of the halves
    # Upper half multiplication
  z1 = _quadratic_multiply(x_left, y_left)
    # Lower half multiplication
  z0 = _quadratic_multiply(x_right, y_right)
    # Middle multiplication: (x_left + x_right) * (y_left + y_right)
  middle_product = _quadratic_multiply(add_binary_numbers(x_left, x_right), add_binary_numbers(y_left, y_right))
    # Calculate the middle term by subtracting z1 and z0 from the middle product
  z2 = add_binary_numbers(middle_product, BinaryNumber(-z1.decimal_val - z0.decimal_val))

    # Combine: Apply bit shifts and add the results
  result = add_binary_numbers(add_binary_numbers(bit_shift(z1, n), bit_shift(z2, n//2)), z0)

  return result


    
    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    
    return (time.time() - start)*1000


    
    

