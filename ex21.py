def add(a, b):
    print "%d + %d" % (a, b)
    return a + b

def substract(a, b):
    print "%d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "%d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "%d / %d" % (a, b)
    return a / b

print "Math time!"

age = add(30, 5)
height = substract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "\nAge: %d, height: %d, weight: %d, iq: %d" % (age, height, weight, iq)

print "\nWHAAAAT?!"

what = add(age, substract(height, multiply(weight, divide(iq, 2))))

print "\n42? Nope this time.", what

puzzle = age + height - weight * iq / 2

print "Puzzle:", puzzle
