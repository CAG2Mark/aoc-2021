import ast

data = open("input").read().split("\n")
if not data[-1].strip(): data = data[0:-1]
# data = [int(x) for x in data]


class Node:
    def __init__(self, left, right, val, parent):
        self.left:Node = left
        self.right:Node = right
        self.val:int = val
        self.parent:Node = parent


def create_tree(num) -> Node:
    if not isinstance(num, list):
        return Node(-1, -1, num, None)
    else:
        left = create_tree(num[0])
        right = create_tree(num[1])
        N = Node(left, right, -1, None)
        left.parent = N
        right.parent = N
        return N

def explode(node:Node, depth = 0):
    if node.val == -1:
        if depth < 4:
            return explode(node.left, depth + 1) or explode(node.right, depth + 1)
        else:
            add_left(node, node.left.val)
            add_right(node, node.right.val)
            node.left
            node.right
            node.val = 0
            return True
    return False

def split(node:Node):
    if node.val == -1:
        return split(node.left) or split(node.right)
    elif node.val >= 10:
        val = node.val
        node.val = -1
        node.left = Node(-1, -1, val//2, node)
        node.right = Node(-1, -1, (val+1)//2, node)
        return True
    return False

def add_left(node:Node, val):
    cur = node.parent
    prev = node
    while cur.left is prev:
        if not cur.parent: return
        prev = cur
        cur = cur.parent
    cur = cur.left
    while cur.val == -1:
        cur = cur.right
    cur.val += val

def add_right(node:Node, val):
    cur = node.parent
    prev = node
    while cur.right is prev:
        if not cur.parent: return
        prev = cur
        cur = cur.parent

    cur = cur.right
    while cur.val == -1:
        cur = cur.left
    cur.val += val

def add(num1, num2):
    newNum = Node(num1, num2, -1, None)
    num1.parent = newNum
    num2.parent = newNum
    changed = True
    while changed:
        changed = False
        exploded = explode(newNum)
        while exploded:
            changed |= exploded
            exploded = explode(newNum)
        changed |= split(newNum)
    return newNum

def print_num(num:Node):
    if num.val != -1: print(num.val, end="")
    else:
        print("[", end = "")
        print_num(num.left)
        print(", ", end = "")
        print_num(num.right)
        print("]", end = "")
data = [create_tree(ast.literal_eval(x)) for x in data]
num = data[0]
for i in range(1,len(data)):
    num = add(num, data[i])

def magnitude(num):
    if num.val != -1: return num.val
    return 3*magnitude(num.left) + 2*magnitude(num.right)

print(magnitude(num))


