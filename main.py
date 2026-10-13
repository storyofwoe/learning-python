"""
Multiline strings
"""

# if can be used as an expression
if 0 > 1:
    print("yay!")
else:
    print("nay!")

# is the same as
x = "yay!" if 0 > 1 else "nay!"
print(x)

# ==== LISTS
li = []
other_li = [1, 2, 3] # can start prefilled

li.append(10) # use append to add to end
li.append(100) # li = [10, 100]
li.pop() # removed from end, li = [10]
li.append(1000)
print(li[-1]) # look at last element
del li[1] # Use del to remove arbitrary elements
#use .insert(<index>, <element>) to insert to specific places

li.append(500)
li.extend(other_li) # li = [10, 500, 1, 2, 3]
1 in li # => True

# === TUPLES
# Like lists, but immutable
tup = (1, 2, 3)
tup[0] # => 1
# tup[0] = 3 # Error

type((1))  # => <class 'int'>
type((1,)) # => <class 'tuple'> -- tuples of len 1 need a comma 

# You can unpack tuples/lists into variables
a, b, c = (1, 2, 3) 
print(a, b, c) # => 1 2 3
a, *b, c = (1, 2, 3, 4)
print(b) # => [2, 3]
a, c = c, a # => a = 4, c = 1

# === DICTIONARIES
dict_1 = {"one": 1, "two": 2, "three": 3}
dict_1["one"] # => 1

# keys have to be immutable types: ints, floats, strings, tuples
# invalid_dict = {[1, 2, 3]: "123"} # Error!
valid_dict = {(1, 2, 3): [1, 2, 3]} # values can be any type
valid_dict[(1, 2, 3)] # => [1, 2, 3]

list(dict_1.keys())   # => ["one", "two", "three"] ( have to wrap it in list() )
list(dict_1.values()) # => [1, 2, 3]

# Check for key existence with 'in'
"one" in dict_1  # => True
1 in dict_1      # => False

# dict_1["four"] # KeyError
# Use .get() to avoid KeyError
dict_1.get("one")  # => 1
dict_1.get("four") # => None