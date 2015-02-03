def add(a, b):
    print "Adding %d + %d" % (a, b)
    return a + b

def subtract(a, b):
    print "Subtracting %d - %d" % (a, b)
    return a - b

def multiply(a, b):
    print "Multiplying %d * %d" % (a, b)
    return a * b

def divide(a, b):
    print "Dividing %d / %d" % (a, b)
    return a / b

print "Let's do some math!"

age = add(30,6)
height = subtract(78,4)
weight = multiply(45,2)
iq = divide(262,2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

print "Extra stuff of my own."
print 3 + 4 / 2 + 1
print (3 + 4) / (2 + 1)
print 3 + (4 / 2 + 1)
print ((3 + 4) / 2) + 1
print float( ((3 + 4) / 2) + 1 ) 
print float( ((3.0 + 4) / 2) + 1 ) 
