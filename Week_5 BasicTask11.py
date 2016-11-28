
class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class List(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, n, x): #n is where too insert it (head or tail) // x is the value of the node we are inserting
        # Not actually perfect: how do we prepend to an existing list?
        if n != None:
            x.next = n.next   #1
            n.next = x        #2
            x.prev = n        #
            if x.next != None:
                x.next.prev = x
        if self.head == None:
            self.head = self.tail = x
            x.prev = x.next = None
        elif self.tail == n:
            self.tail = x

    def display(self):
        values = []
        n = self.head
        while n != None:
            values.append(str(n.value))
            n = n.next
        print ("List: ", ",".join(values))

    def remove_value(self, node_value):
        current_item = self.head
        while current_item is not None:
            if current_item.value == node_value:
                if current_item.prev is not None:
                    current_item.prev.next = current_item.next
                    current_item.next.prev = current_item.prev
                else:
                    self.head = current_item.next
                    current_item.next.prev = None
            current_item = current_item.next

if __name__ == '__main__':
    l = List()
    l.insert(None, Node(4))
    l.insert(l.head, Node(6))
    l.insert(l.head, Node(8))
    l.insert(l.tail, Node(9))
    l.remove_value(4)
    l.display()