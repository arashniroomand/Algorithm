def findClosestValueInBst(tree, target):
    current_node = tree
    while current_node is not None:
        final = current_node.value
        if current_node.value < target:
            current_node = current_node.right
        elif current_node.value > target:
            current_node = current_node.left
        elif current_node.value == target:
            break
     
    
    print(final)
         
    
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

         
         

def test_case_1():
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        return root 
        


tree = test_case_1()

result = findClosestValueInBst(tree,12)

