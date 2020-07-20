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
        return self.preorder_search(self.root,find_val)
        pass

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        # Your code goes here
        r=""
        traversal = self.preorder_print(self.root,[])
        for i in traversal:
            r+=str(i)
        return r[::-1]
        pass

    def preorder_search(self, start, find_val):
        """Helper method - use this to create a
        recursive search solution."""
        # Your code goes here
        if start:
            if start.value==find_val:
                return True
            else:
                return self.preorder_search(start.left,find_val) or self.preorder_search(start.right,find_val)
        return False
        pass

    def preorder_print(self, start, traversal):
        """Helper method - use this to create a
        recursive print solution."""
        # Your code goes here
        # if start==self.root:
        if start:
            traversal.append(start.value)
            if start.left:
                self.preorder_print(start.left,traversal)
            if start.right:
                self.preorder_print(start.right,traversal)
        pass
