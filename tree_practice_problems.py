# UC5 – Implement postorder traversal (Left → Right → Root).

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

    def postorder(self, node) -> None:
        """
        Perform postorder traversal.

        Order: Left → Right → Root
        """
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.data, end=" ")


def main() -> None:
    tree = BinaryTree()

    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)

    print("Postorder Traversal:")
    tree.postorder(tree.root)


if __name__ == "__main__":
    main()