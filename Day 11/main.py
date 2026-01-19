from input import puzzleinput
#from testinput import puzzleinput
from dataclasses import dataclass
from typing import Any
question_part = 1

@dataclass
class DeviceNode():
    name: str
    connects_to: list[str]
    def __repr__(self) -> str:
        return f"Name: {self.name} Connects to: {self.connects_to}"
    
#found online
def nested_count(lst, x):
    return lst.count(x) + sum(
        nested_count(l,x) for l in lst if isinstance(l,list))


def input_to_nodes(puzzleinput: str) -> list[DeviceNode]:
    str_list = puzzleinput.splitlines()
    node_list = []
    for str in str_list:
        name, connects_to = str.split(":")
        node_list.append(DeviceNode(name, connects_to.split()))
    return node_list

def node_tree_to_out(node_list: list[DeviceNode]) -> tuple[list[Any], int]:
    tree = []
    you_node = list(filter(lambda d: d.name == "you", node_list))[0]
    tree.append(you_node.name)
    for node_name in you_node.connects_to:
        node = list(filter(lambda d: d.name == node_name, node_list))[0]
        tree.append(follow_tree_to_out(node, node_list))
    count = nested_count(tree, "out")
    return tree, count




def follow_tree_to_out(node: DeviceNode, node_list: list[DeviceNode]) -> list[Any]:
    tree = []
    for node_name in node.connects_to:
        if node_name == "out":
            tree.append(node_name)
        else:
            next_node = list(filter(lambda d: d.name == node_name, node_list))[0]
            tree.append(next_node.name)
            tree.append(follow_tree_to_out(next_node, node_list))
    return tree

node_list = input_to_nodes(puzzleinput)
print(*node_list,sep="\n")

print(*node_tree_to_out(node_list),sep="\n")