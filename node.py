class Node:
    state = None
    nodes = []
    map = []
    depth = 0
    h = 0
    score = 0
    before_operator = None
    blank_pos = 0

    def __repr__(self):
        return str(self.state)

    def __init__(self, state):
        self.state = state
        self.render_map()

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

    def print_state(self):
        print(self.map)
        print("Blank is on postion: " + str(self.blank_pos[0]) + ":" + str(self.blank_pos[1]))

    def gen_next_nodes(self):
        # calculate possibilities
        print("ok")
