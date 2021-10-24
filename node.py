class Node:
    state = None
    nodes = []
    map = []
    depth = 0
    h = 0
    score = 0
    last_operator = None
    blank_pos = 0
    size = [0, 0]

    def __repr__(self):
        return str(self.state)

    def __init__(self, state):
        self.state = state
        self.render_map()
        self.gen_next_nodes()

    def render_map(self):
        temp = self.state.replace("((", "").replace("))", "").split(" ")
        container = []
        x = 0
        y = 0
        for value in temp:
            if ")(" in value:
                tempValue = value.split(")(")
                container.append(tempValue[0])
                self.map.append(container[:])  # ":" to fixed multiple copies in map
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
        self.map.append(container)
        self.size = [x, y + 1]

    def print_state(self):
        for x in self.map:
            for y in x:
                print(y + " ", end="")
            print("")

        print("Size: " + str(self.size[0]) + ":" + str(self.size[1]))
        print("Blank is on position: " + str(self.blank_pos[0]) + ":" + str(self.blank_pos[1]))

    def gen_next_nodes(self):
        possibility = []
        if self.blank_pos[1] != 0:
            possibility.append("HORE")
        if self.blank_pos[0] != 0:
            possibility.append("VLAVO")
        if self.blank_pos[1] != self.size[1]:
            possibility.append("VPRAVO")
        if self.blank_pos[0] != self.size[0]:
            possibility.append("DOLE")
        if self.last_operator in possibility:
            possibility.remove(self.last_operator)
        print(possibility)
