class BinTreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_insert(tree, item):
    if tree == None:
        tree = BinTreeNode(item)
    else:
        if (item < tree.value):
            if (tree.left == None):
                tree.left = BinTreeNode(item)
            else:
                tree_insert(tree.left, item)
        else:
            if (tree.right == None):
                tree.right = BinTreeNode(item)
            else:
                tree_insert(tree.right, item)
    return tree


def postorder(tree):
    if (tree.left != None):
        postorder(tree.left)
    if (tree.right != None):
        postorder(tree.right)
    print (tree.value)


def in_order_recursive(tree):
    if (tree.left != None):
        in_order_recursive(tree.left)
    print (tree.value)
    if (tree.right != None):
        in_order_recursive(tree.right)

def in_order_iterative(tree):

    finished = False
    stack = []
    current_node = tree

    while (finished != True):

        if current_node != None:
             stack.append(current_node)
             current_node= current_node.left
        else:
            try:                 #Using try because if the list is empty the code will break
                current_node = stack[len(stack) - 1]    #Get pointer back to the previous node
                print(current_node.value)               # Print the last node of the branch
                current_node = current_node.right       #Continue on its right
                stack.pop()                             #Removes the last added node
            except:
                finished = True





if __name__ == '__main__':
    t = tree_insert(None, 6)
    tree_insert(t, 10)
    tree_insert(t, 5)
    tree_insert(t, 2)
    tree_insert(t, 3)
    tree_insert(t, 4)
    tree_insert(t, 11)
    print("Recursively print of the tree:")
    in_order_recursive(t)
    print ("Iteratively print of the tree:")
    in_order_iterative(t)