def reverse_number(cab):
  # Reverse the number
  num1 = str(cab)
  reverse = num1[::-1]
  reverse1 = int(reverse)
  # Return the number
  return reverse1
## Example usage:
print(f"El numero es: {reverse_number(1234)}") # Output: 3221
#print(reverse_number(987654321)) # Output: 123456789
