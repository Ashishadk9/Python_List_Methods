names =["John", "Jane", "Doe"]

#delete the item at index 1
del names[1]
print(names)

# delete items from index 1 to index 2
del names[1: 2]
print(names)

# delete the entire list 
del names

# Error! List doesn't exist.
print(names)
