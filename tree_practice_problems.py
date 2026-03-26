# UC7 – Count total number of nodes and leaf nodes in the tree.

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

    def count_nodes(self, node) -> int:
        """
        Count total nodes in tree.
        """
        if node is None:
            return 0

        return 1 + self.count_nodes(node.left) + self.count_nodes(node.right)

    def count_leaves(self, node) -> int:
        """
        Count leaf nodes in tree.
        """
        if node is None:
            return 0

        if node.left is None and node.right is None:
            return 1

        return self.count_leaves(node.left) + self.count_leaves(node.right)


def main() -> None:
    tree = BinaryTree()

    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)

    print(f"Total Nodes: {tree.count_nodes(tree.root)}")
    print(f"Leaf Nodes: {tree.count_leaves(tree.root)}")


if __name__ == "__main__":
    main()