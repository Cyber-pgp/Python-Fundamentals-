# String Indexting
      # String indexing is like picking a specific Lego block from a set knowing its position. 
      # For example, in the word "CAKE", 'C' is at position 0, 'A' is at 1, 'K' is at 2, and 'E' is at 3.
      # We use these positions to grab any letter we want.

word = "CAKE"
print(word[0] # This will print 'C'
print(word[3] # This will print 'E'

      # There's a cool trick! We can use negative numbers to start from the end.
print([-1] # This will print 'E'

      # By using position numbers we can pick out any letters from the word.

# Case 1
# Given the string | s = 'Python' | Use indexing to print the following output:'o''Pyth''yth''nohtyP'

s = 'Python' # index: 0,1,2,3,4,5 - -1,-2,-3,-4, -5, -6, -7

print(s[4] # This will print 'o'

# Slicing Strings
      # With slicing we can get the whole piece of string, not just a character.
      
print(s[0:4] # Grabing from the start up to index 4 but not including index 4 will print 'Pyth'

print(s[1:4] # This will print 'yth'

      # We can use negative numbers to slice from the end backward

print(s[-3:-7] # This will print 'Pyth'

print(s[-3:-6] # This print 'yth'

# Slicing with Step
      # [start:end:step] - This is the form of slicing with step.
      # The step determines how many characters to skip between the 'start' and 'end' indices.

# Grab every second letter in the range from start to index 4
print(s[0:5:2] # The index is from 0 to 5 '0:5' and adding on 'Step' ':2' will grab every second letter from it.
# This will print 'Pto'

print(s[::] # This will print the whole string

      print(s[::2] # This will print the same as [0:5:2], 'Pto'
            
# We can use a negative step to go backwards. Here's the whole string reversed:
      print(s[::-1] # This will print 'nohtyP'

# Combining negative indices and a negative step to reverse a substring
      print(s[-1:-4:-1] # This will print 'noh'

