# Imagine you have a big toy box (that's our list l), and inside this toy box, you have some toys and another smaller toy box. Now, this smaller toy box also has some toys and a secret note that says "hello" (that's the nested list [1,4,'hello'] inside the big list).

# You want to change that secret note from saying "hello" to saying "goodbye". So, what we're going to do is open the big toy box, then open the smaller toy box inside it, find the secret note, and erase "hello" to write "goodbye" instead.

# In the language of our computer, we tell it exactly like this:

# Here's our big toy box with the smaller box inside it and a secret note
l = [3, 7, [1, 4, 'hello']]

# Now, we find the secret note in the smaller box and change it
l[2][2] = 'goodbye'
# Let's break it down like we are building a Lego Tower, piece by piece.
# Our big toy box, l, is like a line of Lego pieces. Each piece has a number, starting from 0, so we can find them easily. 
# So, in l = [3,7,[1,4,'hello']]:
# The first piece, 3, is number 0.
# The second piece, 7, is number 1.
# The third piece is another small Lego box [1,4,'hello'], and it's number 2.
# Now, we want to change "hello" to "goodbye" in the small Lego box. 
# To do this, we first need to get to the small Lego box. 
# Since it's the third piece in our big Lego line, we use l[2] because we started counting from 0, not 1.
# Inside this small Lego box, we again have pieces numbered starting from 0:
# 1 is number 0,
# 4 is number 1,
# and "hello" is number 2.
# To change "hello", we need to find it by its number. 
# We already got to the small box with l[2], 
# and now we say we want the third piece in that small box, which is "hello". 
# So, we use l[2][2] 
# to say, "In the big Lego line, go to the third piece, which is a small box, and then in that small box, go to the third piece, which is our secret note, and that's what we want to change."
# That's why I did l[2][2] = 'goodbye'
# it's like saying, "In our big toy box, go to the third item, which is a smaller box, and in that box, change the third item from 'hello' to 'goodbye'." It's like following a treasure map to find where "X" marks the spot, and then changing the treasure!

print(l)
# Here we can check if it did changed it or not 
# This will print [3, 7, [1, 4, 'goodbye']]
