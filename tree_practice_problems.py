# UC4 – Implement preorder traversal (Root → Left → Right).

from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, data) -> None:
        new_node = Node(data)

        if not self.root:
            self.root = new_node
            return

        queue = deque([self.root])

        while queue:
            current = queue.popleft()

            if not current.left:
                current.left = new_node
                return
            else:
                queue.append(current.left)

            if not current.right:
                current.right = new_node
                return
            else:
                queue.append(current.right)

    def preorder(self, node) -> None:
        """
        Perform preorder traversal.

        Order: Root → Left → Right
        """
        if node:
            print(node.data, end=" ")
            self.preorder(node.left)
            self.preorder(node.right)


def main() -> None:
    tree = BinaryTree()

    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)

    print("Preorder Traversal:")
    tree.preorder(tree.root)


if __name__ == "__main__":
    main()