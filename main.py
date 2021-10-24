from node import Node

input = "((M 2 3)(1 4 5)(8 7 6))"
goal = "((1 2 3)(8 M 4)(7 6 5))"

closed = []
open = []  # blue

root = Node(input, goal)
print("======= Goal =======")
root.print_goal()
print("====== Actual ======")
root.print_state()
print("===== Children =====")
root.gen_next_nodes()
root.print_next_nodes()
