from pprint import pprint

inputs = [
    (2, "Vod", None),
    (4, "Play", 2),
    (5, "Upload", 2),
    (6, "CDN", 4),
    (7, "Transcode", 4),
    (8, "Manufacture", 6),
    (9, "Protocol", 5),
    (10, "Storage", 5)
]

class Node():
    def __init__(self, id, name, parent_id):
        self.id = id
        self.name = name
        self.parent_id = parent_id
        self.children = []

    
unlinked_relationships = set() # children_id, parent_id
nodes = {} # id, value Node

for id, name, parent_id in inputs:
    node = Node(id, name, parent_id)
    if parent_id in nodes: # parent object has been created
        tup = nodes[parent_id] # .get(parent_id, -1)
        parent = tup[1]
        parent.children.append(node)
    else:
        unlinked_relationships.add((id, parent_id))
    nodes[id] = (parent_id, node)
for child_id, parent_id in unlinked_relationships:
    if parent_id == None:
        continue
    else:
        child = nodes[child_id][1]
        parent = nodes[parent_id][1]
        parent.children.append(child)

for key, value in nodes.items():
    if value[0] == None: # no parent_id
        print(value[1])