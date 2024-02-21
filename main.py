class BinaryNumber:
  def __init__(self, n):
      self.decimal_val = n
      self.binary_vec = list('{0:b}'.format(n))

  def __repr__(self):
      return f'decimal={self.decimal_val} binary={"".join(self.binary_vec)}'

def add_binary_numbers(a, b):
  # Simply add two BinaryNumber instances by their decimal values.
  sum_decimal = a.decimal_val + b.decimal_val
  return BinaryNumber(sum_decimal)

def bit_shift(number, shift_by):
  # Shift a BinaryNumber instance left by shift_by bits.
  return BinaryNumber(number.decimal_val << shift_by)

def _quadratic_multiply(x, y):
  # Base case: if the numbers are small enough, multiply directly.
  if x.decimal_val < 2 or y.decimal_val < 2:
      return BinaryNumber(x.decimal_val * y.decimal_val)

  # Determine the size of the numbers.
  n = max(len(x.binary_vec), len(y.binary_vec))
  half_size = (n + 1) // 2  # Adjust for odd lengths

  # Split the binary numbers in half.
  high1, low1 = x.decimal_val >> half_size, x.decimal_val & ((1 << half_size) - 1)
  high2, low2 = y.decimal_val >> half_size, y.decimal_val & ((1 << half_size) - 1)

  # Recursive multiplication of the halves.
  z0 = _quadratic_multiply(BinaryNumber(low1), BinaryNumber(low2))
  z1 = _quadratic_multiply(BinaryNumber(high1), BinaryNumber(high2))

  # Combine the pieces.
  z2 = _quadratic_multiply(BinaryNumber(low1 + high1), BinaryNumber(low2 + high2))
  z2 = add_binary_numbers(z2, BinaryNumber(-z0.decimal_val - z1.decimal_val))

  return add_binary_numbers(add_binary_numbers(bit_shift(z1, 2 * half_size), bit_shift(z2, half_size)), z0)

def quadratic_multiply(x, y):
  # Ensure both numbers have the same length in binary representation.
  max_len = max(len(x.binary_vec), len(y.binary_vec))
  x_padded = BinaryNumber(x.decimal_val << (max_len - len(x.binary_vec)))
  y_padded = BinaryNumber(y.decimal_val << (max_len - len(y.binary_vec)))

  # Call the internal quadratic multiply function.
  result = _quadratic_multiply(x_padded, y_padded)
  return result.decimal_val

# Testing the corrected implementation
print(quadratic_multiply(BinaryNumber(4), BinaryNumber(4))) 


    
    
def test_quadratic_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    
    return (time.time() - start)*1000


    
    

