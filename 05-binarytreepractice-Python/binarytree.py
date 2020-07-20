class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        # Your code goes here
        if find_val==self.root.value:
            return True
        if self.root.value is None:
            return False
        elif find_val<self.root.value:
            if self.root.left is not None:
                self.preorder_search(self.root.left,find_val)
            else:
                return False
        else:
            if self.root.right is not None:
                self.preorder_search(self.root.right,find_val)
            else:
                return False
        pass

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        pass

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        # Your code goes here
        if find_val==start.value:
            return True
        elif find_val<=start.value:
            if start.left is not None:
                self.preorder_search(self.root.left,find_val)
            else:
                return False
        else:
            if start.right is not None:
                self.preorder_search(self.root.right,find_val)
            else:
                return False
        pass

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        # Your code goes here
        pass
