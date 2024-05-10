class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def inorder_non_recursive(root):
    stack = []
    current = root

    while current or stack:
        while current:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end="->")
        current = current.right

def preorder_non_recursive(root):
    stack = [root]

    while stack:
        current = stack.pop()
        if current:
            print(current.data, end="->")

            # Note: Push right child first, so it gets processed after the left child
            stack.append(current.right)
            stack.append(current.left)


def postorder_non_recursive(root):
    stack = []
    result_stack = []  # To reverse the result

    stack.append(root)

    while stack:
        current = stack.pop()
        if current:
            result_stack.append(current.data)

            # Note: Push left child first, so it gets processed after the right child
            stack.append(current.left)
            stack.append(current.right)

    # Print the result in reverse order to get postorder traversal
    while result_stack:
        print(result_stack.pop(), end="->")

root = Tree(1)
root.left = Tree(2)
root.right = Tree(3)
root.left.left = Tree(4)
root.left.right = Tree(5)

print("Preorder traversal (non-recursive):")
preorder_non_recursive(root)
print("null")

print("\nInorder traversal (non-recursive):")
inorder_non_recursive(root)
print("null")

print("\nPostorder traversal (non-recursive):")
postorder_non_recursive(root)
print("null") 
