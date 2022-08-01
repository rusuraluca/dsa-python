def BinaryTree(r):
    return [r, [], []]


def insertLeft(r, branch):
    # get left child of root
    t = r.pop(1)

    if len(t) > 1:
        r.insert(1, [branch, t, []])

    else:
        r.insert(1, [branch, [], []])

    return r


def insertRight(r, branch):
    # get right child of root
    t = r.pop(2)

    if len(t) > 1:
        r.insert(2, [branch, [], t])

    else:
        r.insert(2, [branch, [], []])

    return r


def getRootValue(r):
    return r[0]


def setRoot(r, value):
    r[0] = value


def getLeftChild(r):
    return r[1]


def getRightChild(r):
    return r[2]


r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertRight(r, 6)
insertRight(r, 7)
print(r)

l = getLeftChild(r)
print(l)

setRoot(l, 9)
print(r)
