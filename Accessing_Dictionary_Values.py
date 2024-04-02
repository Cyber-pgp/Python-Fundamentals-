# Accessing Dictionay

    # Imagine you have a magical book that tells you where all your toys are. You just need to say the name of the toy, and the book tells you exactly where it is. 
    # This magical book is like a dictionary in our computer world. Each toy's name is a "key," and where it tells you the toy is, that's the "value."
    # For example, if you have a toy car and it's under your bed, the book (or dictionary) would look something like this in our computer language:

toy_location = {'toy car': 'under the bed'}
    # If you ask, "Where is my toy car?" you're using the key 'toy car' to find out the value 'under the bed'.

    # Here's how we ask our magical book (or dictionary) in Python:
print(toy_location['toy car'])

    # This tells the computer, "Please tell me where my toy car is," and it answers, "under the bed."

    # Let's say you also have a doll and a ball, and you want to add those to your magical book:

toy_location['doll'] = 'in the toy box'
toy_location['ball'] = 'in the garden'

    # Now, if you want to know where your doll is, you ask:
print(toy_location['doll'])
    # And the computer will tell you, "in the toy box."

    # So, every time you want to know where something is, you just use the magical book (or dictionary) to find out! 
    # It's like a treasure map for finding your toys.
