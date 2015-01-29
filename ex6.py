#set x as a string with placeholder for value 10
x = "There are %d types of people." % 10

#set some strings
binary = "binary"
do_not = "don't"

# set y as string with placeholders
y = "Those who know %s and those who %s." % (binary, do_not)

#echo the output
print x
print y

#and again, with placeholders
print "I said: %r" % x
print "I also said: %s" % y

#set a boolean
hilarious = False

#set a string with a placeholder
joke_evaluation = "Isn't that joke funny?! %r"

#echo string with placeheld value
print joke_evaluation % hilarious

#define 2 strings
w = "This is the left side of ..."
e = "a string with a right side"

#echo them out together
print w + e 
