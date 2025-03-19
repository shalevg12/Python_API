# Shalev Gabay
# Targil 2:


def make_tree(self,left,right):
    def dispatch(x):
        if x == 0:
            return self
        if x == 1:
            return left
        if x == 2:
            return right
        if x == 3:
            return None
    return dispatch

def value(x):
    return x(0)

def left(x):
    return x(1)
def right(x):
    return x(2)
def print_tree(x):
    if x:
        print_tree(left(x))
        print(value(x))
        print_tree(right(x))


def count_value(tree,x):
    if tree == None:
        return 0
    elif value(tree) == x:
        return 1 + count_value(left(tree),x) + count_value(right(tree),x)
    else:
        return count_value(left(tree),x)+count_value(right(tree),x)

def tree_BST(x):
    if x != None:
        if left(x) != None and value(x) <= value(left(x)):
            return False
        if right(x) != None and value(x) >= value(right(x)):
            return False
        return (tree_BST(right(x)))
    return True


def tree_depth(x):
    #print("val:", value(x))
    if left(x) and right(x):
        return (tree_depth(left(x))) + 1 and (tree_depth(right(x))) + 1
    elif left(x):
        return 1 + tree_depth(left(x))
    elif right(x):
        return 1 + tree_depth(right(x))
    else:
        return 0


def tree_Balanced(x):
    # Base condition
    if x is None:
        return True

    # for left and right subtree height
    lh = tree_depth(left(x))
    rh = tree_depth(right(x))

    # allowed values for (lh - rh) are 1, -1, 0
    if (abs(lh - rh) <= 1):
        if tree_Balanced(left(x)) is True:
            if tree_Balanced(right(x)) is True:
                return True
    return False
# Main:

tree1=make_tree(12,make_tree(6,make_tree(8,None,None),None),make_tree(7,make_tree(8,None,None),make_tree(15,None,None)))

tree2=make_tree(12,make_tree(6,make_tree(3,make_tree(1,None,None),None),make_tree(8,make_tree(7,None,None),None)),make_tree(15,None,make_tree(20,make_tree(17,None, None),None)))

print(tree1)
print(tree2)

#print(value(tree1)) # 12
#print(value(left(tree1))) # 6
#print(value(right(left(tree2)))) # 8
print(end="\nTree 1:\n") # Tree 1:
print_tree(tree1) # 8 6 12 8 7 15
print(end="\nTree 2:\n") # Tree 2:
print_tree(tree2) # 1 3 6 7 8 12 15 17 20

print(count_value(tree1,8))
print("\nTree BST:")
print("Tree 1: ",tree_BST(tree1)) # False
print("Tree 2: ",tree_BST(tree2)) # True

print("\nTree Depth:")
print("Tree 1: ",tree_depth(tree1))
print("Tree 2: ",tree_depth(tree2))

print("Tree Balanced:")
#print("Tree 1:",tree_Balanced(tree1))
#print("Tree 2:",tree_Balanced(tree2))

print(count_value(tree1,8))