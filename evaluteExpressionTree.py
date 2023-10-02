
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

         
         
def evaluateExpressionTree(tree):
    if tree.value >= 0:
        return tree.value
    
    leftValue = evaluateExpressionTree(tree.left)
    rightValue = evaluateExpressionTree(tree.right)
    
    if tree.value == -1:
        return leftValue + rightValue
    if tree.value == -2:
        return leftValue - rightValue
    if tree.value == -3:
        return int(leftValue / rightValue)
    
    return leftValue + rightValue
    
    
    

def test_case_1():
        root = BST(-1)
        root.left = BST(-2)
        root.left.left = BST(-4)
        root.left.left.left = BST(2)
        root.left.right = BST(2)
        root.right = BST(-3)
        root.right.left = BST(8)
        root.right.right = BST(3)
        return root 
        


tree = test_case_1()

