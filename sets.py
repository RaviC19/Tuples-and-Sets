# Sets do not have duplicate values and aren't ordered
s = set({1, 2, 3, 4, 5, 5, 5})  # returns {1,2,3,4,5}

# Creating sets
r = set({1, 4, 5})
# or
r = {1, 4, 5}
# can use in to check if a value exists in a set
4 in r  # True

# Use loops to access all the values in a set
numbers = {1, 2, 3, 4}
for number in numbers:
    print(number)


cities = ["London", "Birmingham", "Manchester",
          "Edinburgh", "London", "Tokyo", "Osaka", "Tokyo"]

print(len(set(cities)))
print(list(set(cities)))
