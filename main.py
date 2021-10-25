from node import Node
from datetime import datetime
import random


def get_random_state(m, n):
    result = ["M"]
    for num in range(1, m * n):
        result.append(num)
    random.shuffle(result)
    resultString = "("

    resultIndex = 0
    for y in range(m):
        resultString += "("
        for x in range(n):
            resultString += str(result[resultIndex])
            resultIndex += 1
            if x != n - 1:
                resultString += " "

        resultString += ")"

    resultString += ")"
    return resultString


start_time = datetime.now()
input = get_random_state(3, 3)
goal = get_random_state(3, 3)
# input = "((M 1 2)(3 4 5))"
# goal = "((3 4 5)(M 1 2))"


input = "((M 1 2)(3 4 5)(6 7 8))"
goal = "((8 M 6)(5 4 7)(2 3 1))"

# input = "((M 2 3)(1 4 5)(8 7 6))"
# input = "((1 2 3)(4 M 5)(8 7 6))"
# goal = "((1 2 3)(8 M 4)(7 6 5))"

root = Node(input, goal)
print("======= START ======")
root.print_state()
#
print("======= Goal =======")
root.print_goal()

closed = []
opened = [root]  # blue

nodeCount = 0
thisNode = root
while thisNode.heuristic > 0:
    nodeCount += 1
    # print("===== To Use =====")
    # thisNode.print_state()
    opened.remove(thisNode)
    closed.append(thisNode)

    nodes = thisNode.gen_next_nodes()

    for node in nodes:
        opened.insert(0, node)

    # print("==== actual ====")
    # print("Opened list:", len(open))
    # print(open)
    # print("Closed list:", len(closed))
    # print(open)
    # thisNode.print_next_nodes()
    # closed.append(thisNode)

    # find best price
    bestNode = opened[0]
    for actualNode in opened:
        if actualNode.get_price() < bestNode.get_price():
            bestNode = actualNode

    thisNode = bestNode

    # print refreshing status
    print("\r", f"> Node Num. {nodeCount} "
                f"| Depth: {thisNode.depth} "
                f"| Time: {format(datetime.now() - start_time)[:-5]}"
                f"| Average: {(datetime.now() - start_time) / nodeCount}/node",
          end="")

print("\n======= FINISH =======")
thisNode.print_state()

# solution found
moves = ""
steps = 0
while thisNode is not None:
    if thisNode.last_operator is not None:
        moves = " > " + thisNode.last_operator + moves
        steps += 1
    thisNode = thisNode.parent_node

print("======= RESULT =======")
print(moves[3:])
print("Steps:", steps)
print("Opened list:", len(opened))
print("Closed list:", len(closed))
print("Nodes:", nodeCount)
print('Duration: {}'.format(datetime.now() - start_time))
print(f"Avery time per Node:", (datetime.now() - start_time) / nodeCount)
