class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Manually adding nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

# In-order traversal function
def inorder_traversal(node):
    if node:
        # Traverse the left subtree
        inorder_traversal(node.left)
        
        # Print the current node's data
        print(node.data, end=" -> ")
        
        # Traverse the right subtree
        inorder_traversal(node.right)

# Pre-order traversal function
def preorder_traversal(node):
    if node:
        # Print the current node's data
        print(node.data, end=" -> ")
        
        # Traverse the left subtree
        preorder_traversal(node.left)
        
        # Traverse the right subtree
        preorder_traversal(node.right)

# Post-order traversal function
def postorder_traversal(node):
    if node:
        # Traverse the left subtree
        postorder_traversal(node.left)
        
        # Traverse the right subtree
        postorder_traversal(node.right)
        
        # Print the current node's data
        print(node.data, end=" -> ")

# Perform traversals starting from the root
print("In-order Traversal:")
inorder_traversal(root)
print("null")

print("\nPre-order Traversal:")
preorder_traversal(root)
print("null")

print("\nPost-order Traversal:")
postorder_traversal(root)
print("null")
