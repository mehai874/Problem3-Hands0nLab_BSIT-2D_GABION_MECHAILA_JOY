# Problem 2: Height & Size Toolkit

from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.data] + inorder(node.right)


def preorder(node):
    if node is None:
        return []
    return [node.data] + preorder(node.left) + preorder(node.right)


def postorder(node):
    if node is None:
        return []
    return postorder(node.left) + postorder(node.right) + [node.data]


def level_order(root):
    if root is None:
        return []

    result = []
    queue = deque([root])

    while queue:
        node = queue.popleft()
        result.append(node.data)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result


def size(node):
    if node is None:
        return 0
    return 1 + size(node.left) + size(node.right)


def height(node):
    # Height is measured in edges.
    # An empty tree has height -1.
    if node is None:
        return -1

    left_height = height(node.left)
    right_height = height(node.right)

    return 1 + max(left_height, right_height)


def iterative_size(root):
    if root is None:
        return 0

    count = 0
    queue = deque([root])

    while queue:
        node = queue.popleft()
        count += 1

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return count


# Build the same tree from Problem 1
root = Node(15)
root.left = Node(10)
root.right = Node(25)

root.left.left = Node(4)
root.left.right = Node(12)
root.right.left = Node(20)
root.right.right = Node(30)

root.left.left.left = Node(2)
root.left.left.right = Node(6)


# Display the traversals and toolkit results
print("Inorder:    ", *inorder(root))
print("Preorder:   ", *preorder(root))
print("Postorder:  ", *postorder(root))
print("Level-order:", *level_order(root))

print("Size:", size(root))
print("Height:", height(root))
print("Iterative Size:", iterative_size(root))
