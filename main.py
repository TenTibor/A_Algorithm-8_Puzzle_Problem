import sys

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
# goal = "((3 4 5)(0 1 2))"

root = Node(input, goal)
print("======= START ======")
root.print_state()

print("======= Goal =======")
root.print_goal()

closed = []
open = [root]  # blue

nodeCount = 0
thisNode = root
while thisNode.heuristic > 0:
    # print("===== To Use =====")
    # thisNode.print_state()
    open.remove(thisNode)
    closed.append(thisNode)

    nodes = thisNode.gen_next_nodes()
    for node in nodes:
        # add unique nodes
        if node.is_not_in(closed):
            open.append(node)

    # print("==== actual ====")
    # print("Opened list:", len(open))
    # print(open)
    # print("Closed list:", len(closed))
    # print(open)
    # thisNode.print_next_nodes()
    # closed.append(thisNode)

    # find best price
    bestNode = open[0]
    for actualNode in open:
        if actualNode.get_price() < bestNode.get_price():
            bestNode = actualNode

    thisNode = bestNode

    # print status
    # sys.stdout.write("\033[K")
    print("\r", f"> Node Num. {nodeCount} | Depth: {thisNode.depth} | Time: {format(datetime.now() - start_time)[:-3]}",
          end="")
    nodeCount += 1

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
print("Opened list:", len(open))
print("Closed list:", len(closed))
print('Duration: {}'.format(datetime.now() - start_time))
