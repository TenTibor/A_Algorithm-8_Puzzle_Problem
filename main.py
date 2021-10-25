from node import Node

input = "((4 1 3)(M 2 5)(8 7 6))"
goal = "((1 2 3)(8 M 4)(7 6 5))"

root = Node(input, goal)
print("======= Goal =======")
root.print_goal()

closed = []
open = [root]  # blue

thisNode = root
while thisNode.heuristic > 0:
    print("===== To Use =====")
    thisNode.print_state()
    open.remove(thisNode)
    closed.append(thisNode)

    nodes = thisNode.gen_next_nodes()
    for node in nodes:
        # add unique nodes
        if node.is_not_in(closed):
            open.append(node)

    print("==== actual ====")
    print("Opened list:", len(open))
    print(open)
    print("Closed list:", len(closed))
    # print(open)
    # thisNode.print_next_nodes()
    # closed.append(thisNode)

    # find best price
    bestNode = open[0]
    for actualNode in open:
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
print("Opened list:", len(open))
print("Closed list:", len(closed))
