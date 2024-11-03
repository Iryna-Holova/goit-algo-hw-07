"""
This module implements a basic binary search tree data structure.

Classes:
    Node: Represents a single node in the binary search tree.
    BinarySearchTree: Represents the binary search tree itself.
"""


class Node():
    """
    Represents a single node in the binary search tree.

    Attributes:
        data (int): The value stored in the node.
        left_child (Node): The left child of the node.
        right_child (Node): The right child of the node.
    """
    def __init__(self, data):
        """
        Create a new binary search tree node with given data.

        Args:
            data (int): The value to store in the node.
        """
        self.data = data
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        """
        Return a string representation of the node.

        Returns:
            str: The string representation of the node.
        """
        return str(self.data)


class BinarySearchTree():
    """
    Represents a binary search tree data structure.

    Attributes:
        root (Node): The root node of the binary search tree.
    """
    def __init__(self):
        self.root = None

    def insert(self, data):
        """
        Insert a new node with given data into the binary search tree.

        Args:
            data (int): The value to insert into the tree.
        """
        if not self.root:  # If root is empty then it is the first node
            print(f'Node {data} inserted as the root')
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        """
        Insert a new node with given data into the binary search tree.

        Args:
            data (int): The value to insert into the tree.
            node (Node): The node to insert into the tree.
        """
        if data < node.data:
            if node.left_child:
                self.insert_node(data, node.left_child)
            else:
                print(f'Node {data} inserted')
                node.left_child = Node(data)

        else:
            if node.right_child:
                self.insert_node(data, node.right_child)
            else:
                print(f'Node {data} inserted')
                node.right_child = Node(data)

    def remove(self, data):
        """
        Remove a node with given data from the binary search tree.

        Args:
            data (int): The value to remove from the tree.
        """
        if self.root:
            self.root = self.remove_node(data, self.root)

    def remove_node(self, data, node):
        """
        Remove a node with given data from the binary search tree.

        Args:
            data (int): The value to remove from the tree.
            node (Node): The node to iterate down the tree.

        Returns:
            Node: The root of the modified binary search tree.
        """
        if not node:
            return node

        if data < node.data:
            node.left_child = self.remove_node(data, node.left_child)
        elif data > node.data:
            node.right_child = self.remove_node(data, node.right_child)
        else:
            if not node.left_child and not node.right_child:
                print(f"Node {node.data} removed")
                del node
                return None
            if not node.left_child:
                print(f"Node {node.data} removed")
                temp_node = node.right_child
                del node
                return temp_node

            if not node.right_child:
                print(f"Node {node.data} removed")
                temp_node = node.left_child
                del node
                return temp_node

            print(f"Node {node.data} removed")
            temp_node = self.get_predecessor(node.left_child)
            node.data = temp_node.data
            node.left_child = self.remove_node(temp_node.data, node.left_child)
        return node

    def get_predecessor(self, node):
        """
        Get the predecessor of the given node.

        Args:
            node (Node): The node to get the predecessor of.

        Returns:
            Node: The predecessor of the given node.
        """
        if node.right_child:
            return self.get_predecessor(node.right_child)
        return node

    def get_min_value(self):
        """
        Get the minimum value in the binary search tree.

        Returns:
            int | None: The minimum value in the binary search tree or None if
            the tree is empty.
        """
        if self.root:
            return self.get_min(self.root)
        return None

    def get_min(self, node):
        """
        Get the minimum value in the binary search tree.

        Args:
            node (Node): The node to start the search from.

        Returns:
            int: The minimum value in the binary search tree starting from the
            given node.
        """
        if node.left_child:
            return self.get_min(node.left_child)
        return node.data

    def get_max_value(self):
        """
        Get the maximum value in the binary search tree.

        Returns:
            int | None: The maximum value in the binary search tree or None if
            the tree is empty.
        """
        if self.root:
            return self.get_max(self.root)
        return None

    def get_max(self, node):
        """
        Get the maximum value in the binary search tree.

        Args:
            node (Node): The node to start the search from.

        Returns:
            int: The maximum value in the binary search tree starting from the
            given node.
        """
        if node.right_child:
            return self.get_max(node.right_child)
        return node.data

    def traversal(self):
        """
        Perform a pre-order traversal of the binary search tree and store the
        nodes in the given list.

        Args:
            path (list): The list to store the nodes in.
        """
        if self.root:
            path = []
            self.pre_order_traversal(self.root, path)
            return path

    def pre_order_traversal(self, node, path):
        """
        Perform a pre-order traversal of the binary search tree and store the
        nodes in the given list.

        Args:
            node (Node): The node to start the traversal from.
            path (list): The list to store the nodes in.
        """
        if node:
            path.append(node)
            self.pre_order_traversal(node.left_child, path)
            self.pre_order_traversal(node.right_child, path)

    def search(self, data):
        """
        Search for a node with given data in the binary search tree.

        Args:
            data (int): The value to search for.

        Returns:
            Node | None: The node with the given data or None if not found.
        """
        return self.search_node(data, self.root)

    def search_node(self, data, node):
        """
        Search for a node with given data in the binary search tree.

        Args:
            data (int): The value to search for.
            node (Node): The node to start the search from.

        Returns:
            Node | None: The node with the given data or None if not found.
        """
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self.search_node(data, node.left_child)
        return self.search_node(data, node.right_child)


# Test example:
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(13)
    bst.insert(14)
    bst.insert(12)
    bst.insert(5)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(1)

    print("Min value:", bst.get_min_value())
    print("Max value:", bst.get_max_value())

    pre_order_path = bst.traversal()
    print("Pre-order traversal:", pre_order_path)

    sum_nodes = sum(node.data for node in pre_order_path)
    print("Sum of nodes:", sum_nodes)
