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
j.insert_child(j)
print(root.value)
print(root.child)
print(root.child[0].value)
print(root.child[1].child[0].value)
print(len(root.child))
