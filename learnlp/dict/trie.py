
class Node:
    def __init__(self, value):
        self.children = {}
        self.value = value
    
    def __add_child(self, char, value, overwrite=False):
        child = self.children.get(char)
        if child is None:
            self.children[char] = Node(value)
        elif overwrite:
            child.value = value

class Trie(Node):
    def __init__(self):
        self.count = 0
        super().__init__(None)

    def __getitem__(self, key):
        node = self
        for i, char in enumerate(key):
            child = node.children[char]
            if child is None:
                return None
            else:
                node = child        
        

    def __setitem__(self, key, value):
        node = self
        for i, char in enumerate(key):
            if i == len(key) - 1:
                self.__add_child(char, value, True)
                self.count = self.count + 1
            else:
                self.__add_child(char, None, False)

    def contain(self, key):
        return self.__getitem__(key) is not None