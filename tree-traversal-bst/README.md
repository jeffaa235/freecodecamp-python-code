# tree-traversal-bst

In this project, we learned about tree traversal and how to build a binary search tree in Python code. This program constructs a binary search tree (BST) given a list of numbers.

A binary search tree starts with a single root node which contains a `key` in this case a number. The root node is attached to two other nodes on its left and right respectively, `node.left` and `node.right`,
where the `node.left.key < node.key` and `node.right.key > node.key`. The two nodes have two sub nodes of their own and so on. 

Given a list of numbers, `bst.insert()` adds the numbers to the BST as a node which is located at the lower end of the tree. To delete a node, `bst.delete()` is called which deletes the node and replaces it 
with the either `node.left` or `node.right`, or the minimum node from its `node.right`. `bst.search(key)` searches for a node with value `key` by recursively searching and comparing each node with the key.
`bst.inorder_traversal()` returns a sorted list by traversing the tree recursively, first by calling  `bst.inorder_traversal(node.left)`, then calling `bst.inorder_traversal(node.right)`. 
Hence, a sorted list of numbers is produced.

## Output
![image](https://github.com/user-attachments/assets/2605fa93-652d-4f8b-a532-539277623356)
