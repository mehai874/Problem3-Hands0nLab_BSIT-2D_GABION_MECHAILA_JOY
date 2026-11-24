# Problem 3: BST from Scratch


class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        current = self.root

        while True:
            if key < current.key:
                if current.left is None:
                    current.left = Node(key)
                    return
                current = current.left

            elif key > current.key:
                if current.right is None:
                    current.right = Node(key)
                    return
                current = current.right

            else:
                # Ignore duplicate keys
                return

    def search(self, key):
        current = self.root

        while current is not None:
            if key == current.key:
                return True
            elif key < current.key:
                current = current.left
            else:
                current = current.right

        return False

    def min_value_node(self, node):
        current = node

        while current.left is not None:
            current = current.left

        return current

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None

        if key < node.key:
            node.left = self._delete(node.left, key)

        elif key > node.key:
            node.right = self._delete(node.right, key)

        else:
            # Case 1: No child or only right child
            if node.left is None:
                return node.right

            # Case 2: Only left child
            if node.right is None:
                return node.left

            # Case 3: Two children
            successor = self.min_value_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)

        return node

    def inorder(self):
        result = []

        def traverse(node):
            if node is None:
                return

            traverse(node.left)
            result.append(node.key)
            traverse(node.right)

        traverse(self.root)
        return result


if __name__ == "__main__":
    bst = BST()

    for key in [50, 30, 70, 20, 40, 60, 80, 35, 45]:
        bst.insert(key)

    print(bst.inorder())       # line A
    print(bst.search(35))      # line B
    print(bst.search(99))      # line C

    bst.delete(20)             # leaf
    bst.delete(40)             # two children

    print(bst.inorder())       # line D
