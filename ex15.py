# use the argv module
from sys import argv

# assign 2 vars from args
script, filename = argv

# open the file 
txt = open(filename)

# display filename
print "Here's your file %r:" % filename
# display file contents
print txt.read()

# prompt user
print "Type the filename again:"
# take in input with a > prompt
file_again = raw_input("> ")

#open the file
txt_again = open(file_again)

# diaplay the content
print txt_again.read()

# close the files
txt.close()
txt_again.close()
