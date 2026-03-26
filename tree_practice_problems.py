# UC10 – Implement Binary Search Tree (BST) with insert and search operations.


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BST:
    """
    Binary Search Tree implementation.
    """

    def __init__(self) -> None:
        self.root = None

    def insert(self, node, data):
        """
        Insert node in BST.

        Time Complexity: O(log n) average
        """
        if node is None:
            return Node(data)

        if data < node.data:
            node.left = self.insert(node.left, data)
        else:
            node.right = self.insert(node.right, data)

        return node

    def search(self, node, target) -> bool:
        """
        Search value in BST.

        Time Complexity: O(log n) average
        """
        if node is None:
            return False

        if node.data == target:
            return True

        if target < node.data:
            return self.search(node.left, target)
        else:
            return self.search(node.right, target)


def main() -> None:
    bst = BST()

    # Insert values
    values = [50, 30, 70, 20, 40, 60, 80]
    for val in values:
        bst.root = bst.insert(bst.root, val)

    # Search values
    print(f"Search 40: {bst.search(bst.root, 40)}")
    print(f"Search 90: {bst.search(bst.root, 90)}")


if __name__ == "__main__":
    main()