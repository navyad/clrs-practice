class Node:

    def __init__(self, key):
        self.key = key
        self.next_node = None
        self.prev_node = None

    def __repr__(self):
        return "Node: {0}".format(self.key)


class LinkList:

    def __init__(self):
        self.head = None

    def prepend(self, key):
        new_node = Node(key)
        if self.head:
            _node = self.head
            new_node.next_node = _node
            _node.prev_node = new_node
        self.head = new_node

    def search(self, key):
       _node = self.head
       while _node and _node.key != key:
           _node = _node.next_node
       return _node

    def display(self):
        _node = self.head
        while _node and (_node.next_node or _node.prev_node):
            print _node
            _node = _node.next_node

link_list =  LinkList()
link_list.prepend(12)
link_list.prepend(13)
link_list.prepend(10)
link_list.display()

print link_list.search(111)
print link_list.search(12)
