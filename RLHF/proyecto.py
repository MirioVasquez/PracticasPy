def reverse_number(invar):
  # Reverse the number
  invarmod = str(invar)
  reverse = invarmod[::-1]
  # Return the variable as an integer or a string
  while True:
    try:
      reverse = int(reverse)
      return reverse
    except ValueError:
      return reverse

# Creating a variable to store the input
variable = input("Type something to see it in backwards: ")

# Givin back the reversed input
print(f"Do you mean? {reverse_number(variable)}")
print(type(reverse_number(variable)))