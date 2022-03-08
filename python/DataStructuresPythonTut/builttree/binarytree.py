class binaryTree:
    def __init__(self, root):
        self.Lchild = None
        self.Rchild = None
        self.key = root
    
    def set_Lchild(self,left):
        """
        since a tree is a recursive data structure, then the children of a parent will 
        also be a tree
        """
        if self.Lchild == None:
            self.Lchild = binaryTree(left)
        else:
            new = binaryTree(left)
            new.Lchild = self.Lchild
            self.Lchild = new


    def set_Rchild(self, right):
        if self.Rchild == None:
            self.Rchild = binaryTree(right)
        else:
            new = binaryTree(right)
            new.Rchild = self.Rchild
            self.Rchild = new
    
    def get_Rchild(self):
        return self.Rchild

    def get_Lchild(self):
        print( self.Lchild)
    
    def set_Root_val(self,new):
        self.key = new
    
    def get_root_val(self):
        return self.key




# the traversal techqniques for trees above 
# are explained below


#preorder In a preorder traversal, we visit the root
#  node first, then recursively do a preorder
#traversal of the left subtree, 
# followed by a recursive preorder traversal of the 
# right subtree.

def preodr_trav(tree):
    if tree:
        print(tree.get_root_val())
        preodr_trav(tree.get_Lchild()) # the left nodes will first be searched recusively, then 
        preodr_trav(tree.get_Rchild()) # the right nodes in the tree will be searched butb starting from the root

#inorder In an inorder traversal, 
#we recursively do an inorder traversal on the left
#subtree, visit
#the root node, 
# and finally do a recursive inorder traversal 
# of the right subtree

def Inord_trav(tree):
    if tree != None:
        Inord_trav(tree.get_left_child())
        print(tree.get_root_val())
        Inord_trav(tree.get_Rchild())



# postorder In a postorder traversal, 
# we recursively do a postorder traversal of the left 
# subtree
# and the right subtree followed by a
#  visit to the root node

def postOrd_trav(tree):
    if tree != None:
        postOrd_trav(tree.get_left_child())
        postOrd_trav(tree.get_right_child())
        print(tree.get_root_val())
        


"""root = binaryTree(5)
root.set_Lchild(6)
root.set_Rchild(7)

root.get_Lchild()
root.get_Rchild()
print(root.get_root_val())
print(root.get_Lchild())
print(root.get_Rchild())
"""

r = binaryTree('a')
print(r.get_root_val())
print(r.get_Lchild())
r.set_Lchild('b')
print(r.get_Lchild())





