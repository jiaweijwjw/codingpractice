# [
# {
#   node: "a",
#   children: {
#                       node: "b",
#                       link: "a-b",
#                       children: {
#                                            node: "c",
#                                            link: "a-b-c",
#                                            children: {}
#                                          }
#                      },
#   link: {},
# },
# {
#   node: "d",
#   children: {
#                       node: "e",
#                       link: "d-e",
#                       children: {}
#                     }
# }
# ]

class Node():
    def __init__(self, name, link=None) -> None:
        self.name = name
        self.children = set()
        self.link = set()
        if link:
            self.link.add(link)

class Relationship():
    def __init__(self, rs_list) -> None:
        self.rs_list = rs_list
        self.relationships = {}

    def build_relationships(self):
        for rs in self.rs_list:
            parent, child = rs.split('-')
            parent_node = self.relationships[Node(parent)] if self.relationships[Node(parent)] else Node(parent)
            child_node = Node(child, rs)
            parent_node.children.add(child_node)
            

    def print_relationships(self):
        print(self.rs)



if __name__ == "__main__":
    # rs_list = ["a-b", "b-c", "d-e"]
    # relationship = Relationship(rs_list)
    # relationship.build_relationships()
    # relationship.print_relationships()
    my_dict = {}
    my_dict["fuck"] = 2
    my_dict["you"] = "lmao"
    print(my_dict)