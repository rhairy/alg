class Node:
    def __init__(self, left=None, right=None, value=None):
        self._left = left
        self._right = right
        self._value = value
    
    @property
    def left(self):
        return self._left
        
    @left.setter
    def left(self, Node):
        self._left = Node
        
    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, Node):
        self._right = Node
        
    @property
    def value(self):
        return self._value
        
    @value.setter
    def value(self, value):
        self._value = value
        
    def __repr__(self):
        if self.left is None:
            lv = None
        else:
            lv = self.left.value
            
        if self.right is None:
            rv = None
        else:
            rv = self.right.value
            
        return "{} <= {} => {}".format(lv, self.value, rv)
        
class Tree:
    def __init__(self, left=None, right=None, value=None):
        self._root = Node(left=left, right=right, value=value)
        
        self._root.left=Node(value='b')
        self._root.right=Node(value='c')
        
        b = self._root.left
        b.left = Node(value="d")
        b.right = Node(value="e")
        
        c = self._root.right
        c.right = Node(value="f")
        
        # print(self._root)
        # print(b)
        # print(c)
        # print(b.left)
        # print(b.right)
        # print(c.right)
        
    def depth_traverse(self):
        stack = []
        stack.append(self._root)
        
        while len(stack) > 0:
            node = stack.pop()
            print(node)
            if node.right is not None:
                stack.append(node.right)
            if node.left is not None:
                stack.append(node.left)
                
    def breadth_traverse(self):
        queue = []
        queue.append(self._root)
        
        while len(queue) > 0:
            node = queue.pop(0)
            print(node)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
                
        
        
        
    def __repr__(self):
        return repr(self._root)
        
if __name__ == '__main__':
    t = Tree(value='a')
    print("depth first traversal")
    t.depth_traverse()
    
    print("breadth first traversal")
    t.breadth_traverse()
    