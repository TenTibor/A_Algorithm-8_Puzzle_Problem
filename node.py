class Node:
    state = None
    nodes = []
    map = []
    depth = 0
    h = 0
    score = 0
    before_operator = None

    def __repr__(self):
        return str(self.state)

    def __init__(self, state):
        self.state = state
        self.render_map()

    def render_map(self):
        temp = self.state.replace("((", "").replace("))", "").split(" ")
        container = []
        for value in temp:
            if ")(" in value:
                tempValue = value.split(")(")
                container.append(tempValue[0])
                self.map.append(container[:])  # ":" to fixed multiple copies in map
                container.clear()
                container.append(tempValue[1])
            else:
                container.append(value)
        self.map.append(container)

    def print_state(self):
        print(self.state)
        print(self.map)

    # def gen_next_nodes(self):
    #     calculate possibilities

