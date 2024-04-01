# String indexing is like picking a specific Lego block from a set knowing its position. 
# For example, in the word "CAKE", 'C' is at position 0, 'A' is at 1, 'K' is at 2, and 'E' is at 3.
# We use these positions to grab any letter we want.

word = "CAKE"
print(word[0] # This will print 'C'
print(word[3] # This will print 'E'
# There's a cool trick! We can use negative numbers to start from the end.
print([-1] # This will print 'E'

# By using position numbers we can pick out any letters from the word.

# Lab 1
# Given the string | s = 'Python' | Use indexing to print the following output:'o''Pyth''yth''nohtyP'

s = 'Python' # index: 0,1,2,3,4,5 - -1,-2,-3,-4, -5, -6, -7
print(s[4] # This will print 'o'

# Slicing Strings - with slicing we can get the whole piece of string, not just a character.
print(s[0:4] # Grabing from the start up to index 4 but not include index 4 will print 'Pyth'

print(s[1:4] # This will print 'yth'

# We can use negative numbers to slice from the end backward
print(s[-3:-7] # This will print 'Pyth'

print(s[-3:-6] # This print 'yth'

      
