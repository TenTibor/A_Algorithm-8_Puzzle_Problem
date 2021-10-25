from node import Node

input = "((4 1 3)(M 2 5)(8 7 6))"
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
steps = 0
while thisNode is not None:
    if thisNode.last_operator is not None:
        moves = " > " + thisNode.last_operator + moves
        steps += 1
    thisNode = thisNode.parent_node
print(moves[3:])
print("Steps:", steps)
