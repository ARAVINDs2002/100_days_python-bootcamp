from collections import deque

def are_parentheses_balanced(s):
    # Create a deque to store opening parentheses
    stack = deque()
    
    # Define matching pairs of parentheses (closing to opening)
    matching_pairs = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    # Iterate through each character in the string
    for char in s:
        # If it's an opening parenthesis, push it onto the deque
        if char in '({[':
            stack.append(char)
        # If it's a closing parenthesis, check the matching opening parenthesis
        elif char in ')}]':
            if not stack or stack.pop() != matching_pairs[char]:
                # If there's no opening parenthesis or the matching is incorrect, it's unbalanced
                return False
    
    # If the deque is empty, all parentheses were properly matched
    return len(stack) == 0

# Call the function with a test string
s = are_parentheses_balanced("(a+b)")

# Print the result to check if parentheses are balanced
print("Are parentheses balanced?", s)
