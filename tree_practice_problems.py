# UC1 – Create a Node class to represent elements in a binary tree.

class Node:
    """
    Represents a single node in a binary tree.

    Each node contains:
    - data
    - reference to left child
    - reference to right child
    """

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


def main() -> None:
    """
    Demonstrates creation of tree nodes.
    """
    root = Node(10)
    root.left = Node(20)
    root.right = Node(30)

    print(f"Root: {root.data}")
    print(f"Left Child: {root.left.data}")
    print(f"Right Child: {root.right.data}")


if __name__ == "__main__":
    main()