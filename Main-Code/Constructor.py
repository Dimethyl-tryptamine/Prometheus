
import sys
import os

# This finds the 'Prometheus' directory and adds it to the search path
parent_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if parent_dir not in sys.path:
    sys.path.append(parent_dir)


from Research.node import Node
root = Node("animal", 100)

dog = Node("dog", 40, root)
root.add_child(dog)

print(dog.depth)
print(dog.change_rate)