# add - adds an element to a set. If the element is already in the set, the set doesn't change
s = set([1, 2, 3])
s.add(4)
s  # {1,2,3,4}

# remove - removes a value from the set - returns a KeyError if the value is not found - can use .discard if want to avoid errors
set1 = {1, 2, 3, 4, 5, 6}
set1.remove(3)
print(set1)  # {1,2,4,5,6}

# copy - creates a copy of the set
s = set([1, 2, 3])
another_s = s.copy()
another_s  # {1,2,3}
another_s is s  # False

# clear - removes all the contents of a set
r = set([1, 2, 3, 4, 5, 6])
r.clear()
print(r)  # set()

# union - joins contents of two sets and doesn't duplicate anything
big_cities = {"London", "Tokyo", "New York",
              "Osaka", "Manchester", "Barcelona"}
english_cities = {"Birmingham", "Liverpool",
                  "London", "Manchester", "Nottingham"}
print(big_cities | english_cities)
# {'Tokyo', 'Barcelona', 'London', 'Birmingham', 'Liverpool', 'Nottingham', 'New York', 'Osaka', 'Manchester'}

# intersection - shows what are in both/all the sets
print(big_cities & english_cities)
# returns {'London', 'Manchester'}
