class Node:
    state = None
    goal = None
    nodes = []
    map = []
    goalMap = []
    depth = 0
    heuristic = None
    last_operator = None
    blank_pos = None
    size = [0, 0]

    def __repr__(self):
        return str(self.state)

    def __init__(self, *args):
        # init for ROOT
        if len(args) == 2:
            self.state = args[0]
            self.goalMap = self.render_map(args[1])
            self.map = self.render_map(args[0])
        else:
            # init for CHILD
            self.map = args[0]
            self.goalMap = args[1]
            self.last_operator = args[2]
            self.blank_pos = args[3]
            self.depth = args[4]
        self.calc_heuristic2()

    def render_map(self, state):
        newMap = []
        temp = state.replace("((", "").replace("))", "").split(" ")
        container = []
        x = 0
        y = 0
        for value in temp:
            if ")(" in value:
                tempValue = value.split(")(")
                container.append(tempValue[0])
                newMap.append(container[:])  # ":" to fixed multiple copies in map
                if tempValue[0] == "M":
                    self.blank_pos = [x, y]
                container.clear()
                y += 1
                x = 0
                container.append(tempValue[1])
                if tempValue[1] == "M":
                    self.blank_pos = [x, y]
            else:
                container.append(value)
                if value == "M":
                    self.blank_pos = [x, y]
            x += 1
        newMap.append(container)
        self.size = [x, y + 1]
        return newMap

    def print_goal(self):
        for x in self.goalMap:
            for y in x:
                print(y + " ", end="")
            print("")

    def print_state(self):
        for x in self.map:
            for y in x:
                print(y + " ", end="")
            print("")

        print("Heuristic: " + str(self.heuristic))
        print("Depth: " + str(self.depth))

    def get_possible_moves(self):
        possibilities = []
        if self.blank_pos[1] != 0:
            possibilities.append("HORE")
        if self.blank_pos[0] != 0:
            possibilities.append("VLAVO")
        if self.blank_pos[1] != self.size[1]:
            possibilities.append("VPRAVO")
        if self.blank_pos[0] != self.size[0]:
            possibilities.append("DOLE")
        if self.last_operator in possibilities:
            possibilities.remove(self.last_operator)

        return possibilities

    def calc_heuristic2(self):
        allNumsValue = []
        for y in self.map:
            for x in y:
                if x in allNumsValue:
                    print("")
                elif x == "M":
                    allNumsValue.append(0)
                else:
                    allNumsValue.append(x)
        # print(allNumsValue)

        # find num in goal map
        curX = 0
        curY = 0
        for index, num in enumerate(allNumsValue):
            goalY = 0
            if num != 0:
                for y in self.goalMap:
                    if num in y:
                        goalX = y.index(num)
                        # print("goalY", goalY)
                        # print("currY", curY)
                        hThisX = (goalX - curX) if goalX > curX else curX - goalX

                        hThisY = (goalY - curY) if goalY > curY else curY - goalY

                        allNumsValue[index] = hThisX + hThisY
                        # print(num, ":", allNumsValue[index], "(", hThisX, "+", hThisY, ")")
                        break
                    goalY += 1

            curX += 1
            if curX == 3:
                curY += 1
                curX = 0

        self.heuristic = sum(allNumsValue)

    def gen_next_nodes(self):
        possibilities = self.get_possible_moves()
        print(possibilities)
        # get next node for every possible move
        for possibility in possibilities:

            # gen map after move
            newMap = [row[:] for row in self.map]
            newBlankPos = None
            # calc new blank pos and switch values
            if possibility == "VPRAVO":
                newBlankPos = [self.blank_pos[0], self.blank_pos[1] + 1]
                newMap[self.blank_pos[0]][self.blank_pos[1]] = self.map[newBlankPos[0]][newBlankPos[1]]
            elif possibility == "VLAVO":
                newBlankPos = [self.blank_pos[0], self.blank_pos[1] - 1]
                newMap[self.blank_pos[0]][self.blank_pos[1]] = self.map[newBlankPos[0]][newBlankPos[1]]
            elif possibility == "HORE":
                newBlankPos = [self.blank_pos[0] - 1, self.blank_pos[1]]
                newMap[self.blank_pos[0]][self.blank_pos[1]] = self.map[newBlankPos[0]][newBlankPos[1]]
            elif possibility == "DOLE":
                newBlankPos = [self.blank_pos[0] + 1, self.blank_pos[1]]
                newMap[self.blank_pos[0]][self.blank_pos[1]] = self.map[newBlankPos[0]][newBlankPos[1]]

            newMap[newBlankPos[0]][newBlankPos[1]] = "M"

            self.nodes.append(Node(newMap, self.goalMap, possibility, newBlankPos, self.depth + 1))

    def print_next_nodes(self):
        for node in self.nodes:
            node.print_state()
