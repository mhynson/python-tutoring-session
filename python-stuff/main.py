a = 5
b = 6
c = 100

# Create a function that adds numbers together and returns the sum
def sum (num1, num2):
  theSum = num1 + num2
  return theSum

print( sum(a, c) )


# Create a function that multiplies two numbers and returns the product
def product(numA, numB):
  theProduct = numA * numB
  return theProduct

print( "The product of " + str(a) + " and " + str(b) + " is -> " + str(product(b, a)))