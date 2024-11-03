# Binary Search Tree & Comment System Implementations

This repository contains several completed tasks focused on binary search trees (BST) and a hierarchical comment system. Each task includes core implementations, specific operations, and insights into the structure and algorithmic choices.

Table of Contents

- [Task 1: Find Maximum Value in BST](#task-1-find-maximum-value-in-bst)
- [Task 2: Find Minimum Value in BST](#task-2-find-minimum-value-in-bst)
- [Task 3: Sum of All Values in BST](#task-3-sum-of-all-values-in-bst)
- [Task 4: Hierarchical Comment System](#task-4-hierarchical-comment-system)
- [Insights and Observations](#insights-and-observations)

## Task 1: Find Maximum Value in BST

**Objective**: Implement a function to find the maximum value in a binary search tree.

The maximum value in a BST can be found by traversing to the rightmost node. The `get_max_value` method in the `BinarySearchTree` class locates this node efficiently, providing the maximum integer stored within the tree.

### Code Example

```python
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
max_value = bst.get_max_value()
print("Max value:", max_value)  # Output: Max value: 14
```

## Task 2: Find Minimum Value in BST

**Objective**: Implement a function to find the minimum value in a binary search tree.

Finding the minimum value is achieved by traversing to the leftmost node in the tree. The `get_min_value` method performs this traversal and returns the smallest value in the BST.

### Code Example

```python
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
min_value = bst.get_min_value()
print("Min value:", min_value)  # Output: Min value: 1
```

## Task 3: Sum of All Values in BST

**Objective**: Implement a function to calculate the sum of all values in the BST.

This task uses a pre-order traversal to accumulate all node values in the tree. After traversing the tree with the `traversal` method, the sum is calculated by iterating over the resulting nodes.

### Code Example

```python
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
pre_order_path = bst.traversal()
sum_nodes = sum(node.data for node in pre_order_path)
print("Sum of nodes:", sum_nodes)  # Output: Sum of nodes: 64
```

## Task 4: Hierarchical Comment System

**Objective**: Create a class structure for a comment system, where each comment can have multiple replies in a nested hierarchy.

The `Comment` class supports adding replies, removing comments, and displaying the hierarchy with indentation. Deleted comments are replaced with a standard message, allowing the hierarchy to remain intact.

### Key Methods

- `add_reply`: Adds a new reply to a comment.
- `remove_reply`: Replaces the comment text with a deletion message and flags it as deleted.
- `display`: Recursively prints comments and their replies with indentation to represent hierarchy.

### Code Example

```python
root_comment = Comment("What a wonderful book!", "John")
reply1 = Comment("The book was a disappointment :(", "Jane")
reply2 = Comment("What's so wonderful about it?", "Mary")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("It was a waste of paper...", "Bill")
reply1.add_reply(reply1_1)

reply1.remove_reply()

root_comment.display()
```

### Output

```bash
John: What a wonderful book!
    [deleted]: This comment has been removed.
        Bill: It was a waste of paper...
    Mary: What's so wonderful about it?
```

## Insights and Observations

### Tasks 1-3 (Binary Search Tree) [See code](./bst_tree.py)

- **Efficiency**: Each operation takes advantage of the binary search property, providing efficient `O(log n)` traversal for both finding minimum/maximum values and summing nodes.
- **Tree Structure**: The pre-order traversal used in Task 3 can be replaced with other traversal orders depending on specific needs for accumulating data.

### Task 4 (Comment System) [See code](./comments.py)

- **Modularity**: The `Comment` class structure allows for seamless addition, removal, and nested display of replies.
- **Hierarchy Display**: The recursive display function outputs nested comments, making it suitable for real-world applications such as forums or blog comment sections.

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.
