# Create a list, dictionary, and set
my_list = [1, 2, 3]
my_dict = {'a': 1, 'b': 2, 'c': 3}
my_set = {1, 2, 3}

# Operations on the list
# Adding elements to the list
my_list.append(4)
print("List after adding an element:", my_list)

# Removing elements from the list
my_list.remove(2)
print("List after removing an element:", my_list)

# Modifying elements in the list
my_list[1] = 10  # Changing the second element
print("List after modifying an element:", my_list)

# Operations on the dictionary
# Adding a new key-value pair
my_dict['d'] = 4
print("Dictionary after adding a new element:", my_dict)

# Removing a key-value pair
my_dict.pop('b')
print("Dictionary after removing a key-value pair:", my_dict)

# Modifying a value in the dictionary
my_dict['a'] = 10
print("Dictionary after modifying a value:", my_dict)

# Operations on the set
# Adding an element to the set
my_set.add(4)
print("Set after adding an element:", my_set)

# Removing an element from the set
my_set.discard(1)
print("Set after removing an element:", my_set)

# Sets don't support modifying elements directly, but you can remove and re-add
my_set.discard(2)
my_set.add(5)
print("Set after modifying an element:", my_set)
