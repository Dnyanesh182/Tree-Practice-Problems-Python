# UC8 – Search for a value in the binary tree using DFS.

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

    def dfs_search(self, node, target) -> bool:
        """
        Search value using DFS (recursive).

        Time Complexity: O(n)
        """
        if node is None:
            return False

        if node.data == target:
            return True

        return (
            self.dfs_search(node.left, target) or
            self.dfs_search(node.right, target)
        )


def main() -> None:
    tree = BinaryTree()

    tree.insert(10)
    tree.insert(20)
    tree.insert(30)
    tree.insert(40)
    tree.insert(50)

    target = 40
    print(f"Search {target}: {tree.dfs_search(tree.root, target)}")

    target = 99
    print(f"Search {target}: {tree.dfs_search(tree.root, target)}")


if __name__ == "__main__":
    main()