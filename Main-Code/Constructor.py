import calss node

root = Node("animal", 100)

dog = Node("dog", 40, root)
root.add_child(dog)

print(dog.depth)
print(dog.change_rate)