class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None


class LinkedList: 
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        

class bubblePop():

    def __init__(self):
        self.bubbleList = LinkedList()
    

    def getSize(self):
        if self.bubbleList.size is 0:
            return 0
        time = self.bubbleList.tail.data
        cutoff = time - 5
        curr = self.bubbleList.head
        while curr and curr.data < cutoff:
            head = curr.next
            curr.next = None
            self.bubbleList.size -= 1
            curr = curr.next
        return self.bubbleList.size

    def addBubbles(self, time):
        bubble = Node(time + 5, None)
        if self.bubbleList.head == None:
            self.bubbleList.head = bubble
        if self.bubbleList.tail == None:
            self.bubbleList.tail = bubble
        else: 
            self.bubbleList.tail.next = bubble
            self.bubbleList.tail = self.bubbleList.tail.next
        self.bubbleList.size += 1


# putting 2 bubble (0, 6) -> getSize -> 1

# bubPop.addBubbles(0)
# bubPop.addBubbles(6)
# bubPop.addBubbles(6)
# bubPop.addBubbles(6)
print(bubPop.getSize())

        



