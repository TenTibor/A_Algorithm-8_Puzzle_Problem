from node import Node

input = "((M 1 3)(4 2 5)(8 7 6))"
goal = "((1 2 3)(8 M 4)(7 6 5))"

closed = []
open = []  # blue

root = Node(input, goal)
print("======= Goal =======")
root.print_goal()

thisNode = root
while thisNode.heuristic > 0:
    print("===== To Use =====")
    thisNode.print_state()
    print("===== Children =====")
    nodes = thisNode.gen_next_nodes()
    for node in nodes:
        node.print_state()
    # thisNode.print_next_nodes()
    # closed.append(thisNode)

    # find best price
    bestNode = nodes[0]
    for actualNode in nodes:
        if actualNode.get_price() < bestNode.get_price():
            bestNode = actualNode

    thisNode = bestNode

# solution found
moves = ""
while thisNode is not None:
    if thisNode.last_operator is not None:
        moves = " > " + thisNode.last_operator + moves
    thisNode = thisNode.parent_node
print(moves[3:])
