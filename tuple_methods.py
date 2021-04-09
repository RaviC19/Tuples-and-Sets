# create tuples using () or the tuple function
first_tuple = (1, 2, 3, 3, 4)
second_tuple = tuple(5, 4, 3, 2)

# count - returns the number of times a value appears in a tuple
x = (1, 2, 3, 3, 3)
x.count(1)
x.count(3)

# index - returns the index at which a value is found in a tuple
t = (1, 2, 3, 3, 3)
t.index(1)  # 0
t.index(3)  # 2 -only the first matching index is returned

# can also use slices
