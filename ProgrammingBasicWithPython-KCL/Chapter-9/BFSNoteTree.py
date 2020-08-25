class Node:
    def __init__(self,value):
        self.value = value
        self.child = []
    def __repr__(self):
        return "Value is " + self.value
    def insert_child(self,node):
        self.child.append(node)
    def get_child(self):
        return self.child
    def bfs(self):
        thislevel = [self]
        while thislevel:
            nextlevel = []
            level = []
        for n in thislevel:
            level.append(n.value)
    def insert_child(self,node):
        self.child.append(node)
    def get_child(self):
        return self.child
    def bfs(self):
        thislevel = [self]
        while thislevel:
            nextlevel = []
            level = []
            for n in thislevel:
                level.append(n.value)
            if len(n.child) > 0:
                    print(",".join(level))
                    thislevel = nextlevel
root = Node("A")
b = Node("B")
c = Node("C")
d = Node("D")
root.insert_child(b)
root.insert_child(c)
root.insert_child(d)
e = Node("E")
f = Node("F")
g = Node("G")
b.insert_child(e)
b.insert_child(f)
b.insert_child(g)
h = Node("H")
i = Node("I")
c.insert_child(h)
c.insert_child(i)
j = Node("J")
d.insert_child(j)
root.bfs()
