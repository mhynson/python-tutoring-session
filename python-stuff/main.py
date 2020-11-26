a = 5
b = 6
c = 100


# Create a function that adds numbers together and returns the sum
def sum(num1, num2):
    theSum = num1 + num2
    return theSum


print(sum(a, c))


# Create a function that multiplies two numbers and returns the product
def product(numA, numB):
    theProduct = numA * numB
    return theProduct


print("The product of " + str(a) + " and " + str(b) + " is -> " + str(product(b, a)))


# create a function that subtracts two numbers and returns the difference
def difference(num1, num2):
    theDifference = num1 - num2
    return theDifference


print(str(difference(c, b) + "is the difference between" + float(c) - float(b)))

# create a function that divides two numbers and returns the dividend? Hope thats right lol

def dividend(numX, numT):
  theDividend = numX / numT
  return theDividend


print(dividend(b,a))

# create a function that determines the percentage of 2 numbers

def prcnt(num1, num2):
  thePercentage = num1 % num2
  return thePercentage

print(prcnt(b,c))