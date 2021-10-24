from node import Node

input = "((M 2 3)(1 4 5)(8 7 6))"
goal = "((1 2 3)(8 M 4)(7 6 5))"

root = Node(input, goal)
root.print_state()
