class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
node1=Node(2)
node2=Node(3)
node3=Node(4)

node1.next=node2
node2.next=node3
node3.next=None

head=node1
current=head

while current != None:
    print(current.data,end="->")
    current=current.next
    
    
print("null")    
