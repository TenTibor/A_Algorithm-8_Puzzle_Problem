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

size_of_generated_puzzle = [2, 2]

input = get_random_state(size_of_generated_puzzle[0], size_of_generated_puzzle[1])
goal = get_random_state(size_of_generated_puzzle[0], size_of_generated_puzzle[1])

# EXAMPLE 1
# input = "((M 1 2)(3 4 5))"
# goal = "((3 4 5)(M 1 2))"

# EXAMPLE 2
# input = "((M 1 2)(3 4 5)(6 7 8))"
# goal = "((8 M 6)(5 4 7)(2 3 1))"

# EXAMPLE 3
# input = "((1 M 2)(3 7 4)(8 6 5))"
# goal = "((8 2 3)(M 7 5)(1 6 4))"


root = Node(input, goal)
print("== START ==")
root.print_state()

print("=== Goal ===")
root.print_goal()
print("============")

closed = []
opened = [root]

nodeCount = 0
thisNode = root
while thisNode.heuristic > 0:
    nodeCount += 1

    opened.remove(thisNode)
    closed.append(thisNode)

    nodes = thisNode.gen_next_nodes()

    for node in nodes:
        opened.insert(0, node)

    # find node with lowest function
    bestNode = min(opened, key=lambda x: x.get_price())

    thisNode = bestNode

    # print refreshing status
    print("\r", f"> Node Num. {nodeCount} "
                f"| Depth: {thisNode.depth} "
                f"| Time: {format(datetime.now() - start_time)[:-5]}"
                f"| Average: {(datetime.now() - start_time) / nodeCount}/node",
          end="")

print("\n== FINISH ==")
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
print("Nodes:", nodeCount)
print('Duration: {}'.format(datetime.now() - start_time))
print(f"Avery time per Node:", (datetime.now() - start_time) / nodeCount)
