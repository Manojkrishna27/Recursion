class Tree:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
 # this is preorder traversal of Tree in recursion pattern first it prints root then left and right
def preorder(root):
    if root is None:
        return
    print(root.data,end=" ")
    preorder(root.left)
    preorder(root.right)
root=Tree(1)
root.left=Tree(2)
root.right=Tree(3)
root.left.left=Tree(4)
root.left.right=Tree(5)
preorder(root)