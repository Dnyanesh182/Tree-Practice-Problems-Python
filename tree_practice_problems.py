# UC2 – Create a Binary Tree class and insert nodes into the tree.

from collections import deque


class Node:
    """
    Represents a node in a binary tree.
    """

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    """
    Binary Tree implementation with level-order insertion.
    """

    def __init__(self) -> None:
        self.root = None

    def insert(self, data) -> None:
        """
        Insert node in level-order (BFS style).

        Time Complexity: O(n)
        """
        new_node = Node(data)

        # If tree is empty
        if not self.root:
            self.root = new_node
            print(f"Inserted root: {data}")
            return

        queue = deque([self.root])

        while queue:
            current = queue.popleft()

            # Insert as left child
            if not current.left:
                current.left = new_node
                print(f"Inserted {data} to left of {current.data}")
                return
            else:
                queue.append(current.left)

            # Insert as right child
            if not current.right:
                current.right = new_node
                print(f"Inserted {data} to right of {current.data}")
                return
            else:
                queue.append(current.right)


def main() -> None:
    tree = BinaryTree()

    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)


if __name__ == "__main__":
    main()