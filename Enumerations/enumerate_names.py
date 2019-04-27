#enumerate() allows for index retrieval when iterating an array/list
#this will print out the index and the name in the array at that index

names = ["Matthew", "Mark", "Luke", "John"]

for index, name in enumerate(names) :
    print('{} - {}'.format(str(index), name))
