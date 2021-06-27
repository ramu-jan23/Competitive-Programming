
class Node():
    def __init__(self, _data, _next):
        self.data = _data
        self.next = _next
        
class LinkedList():
    def __init__(self, _list):
        self.head = None
        self.tail = None
        self.count = None
        
        for i in _list:
            self.append(i)
       
    def append(self, _data, pos=None):
        node = Node(_data, None)
        
        if (self.head == None):
            self.head = node
            self.tail = node
            return
        
        if (pos == None):
            self.tail.next = node
            self.tail = node
        else:
            tmp = self.head
            if (pos == 0):
                node.next = tmp
                self.head = node
                return
                
            for i in range(pos-1):
                tmp = tmp.next
                if tmp == None: break
            
            if (tmp == None):
                self.tail.next = node
                self.tail = node
            else:
                node.next = tmp.next
                tmp.next = node
                
                self.tail = node
    
    def pop(self, pos=None):
        
        tmp = self.head
        
        if pos == None:
            while (tmp.next != self.tail):
                tmp = tmp.next
            
            data = tmp.next.data
            self.tail = tmp
            
            del tmp.next
            
            self.tail.next = None
        elif pos == 1:
            data = tmp.data
            self.head = tmp.next
            del tmp
        else:
            for i in range(pos-2):
                tmp = tmp.next
            
            popEle = tmp.next
            data = popEle.data
            tmp.next = popEle.next
            
            if tmp.next == None:
                self.tail = tmp
            
            del popEle
        
        return data
        
    def remove(self, pos):
        self.pop(pos)
        
    def __str__(self):
        ll = ""
        tmp = self.head
        
        while (tmp != None):
            ll += str(tmp.data) + " -> "
            tmp = tmp.next
        return ll
        
    def findNthElement(self, node, pos):
        
        if node == None:
            n = 1
            return n 
        n = self.findNthElement(node.next, pos) 
        if (pos == n):
            print (node.data)
        return n + 1
        
    def findNthElementFromLast(self, pos):
        
        n = self.findNthElement(self.head, pos)
        #print (n)
    
    
    def findNthElementfromEnd(self, pos):
        
        p2 = self.head
        p1= self.head
        while (pos != 0):
            if p2 == None:
                return
            p2 = p2.next
            pos -= 1
            
        while (p2 != None):
            p1 = p1.next
            p2 = p2.next
            
        print (p1.data)
        
    def findMiddleElement(self):
        p1 = self.head
        p2 = self.head
        
        while p2 != None and p2.next != None:
            p1 = p1.next
            p2 = p2.next.next
            
        print ("Middle element :: ", p1.data)
        
    def reverseLinkedList(self):
        
        tmp = self.head
        self.head = None
        self.tail = None
        
        while tmp != None:
            self.append(tmp.data, 0)
            tmp = tmp.next
        
    def isListLoop(self):
        
        tmp = self.head
        for i in range(8):
            tmp = tmp.next
            
        self.tail.next = tmp
        self.tail = tmp
        print ("tail at :: ", self.tail.data)
        
        p1 = self.head
        p2 = p1.next
        
        while (p1 != None and p2 != None and p2.next !=None and p1 != p2):
            p1 = p1.next
            p2 = p2.next.next
            
        if (p1 == p2):
            print ("points crossed at :: ", p1.data)
            
            
        # To verify where the loop starts
        # Find the loop in the list as above
        # Get the node where the two pointers crossed 
        # Create 2 linked lists 1 from Head to Crossed node, another from next of Crossed node to crossed node
        # So 2 lists having same tail and different heads and intersection at some point
        # if both the lists are same int intersection point is same
        # l1 > l2, then leave l1 - l2 nodes and start traversing both lists to meet intersection
        # l2 > l1, then leave l2 - l1 nodes and start traversing both lists to meet intersection
        h1 = self.head
        t1 = p1
        
        h2 = p1.next
        t2 = p1
        p1.next = None
        
        c1 = 0
        tr1 = h1
        while tr1 != None:
            c1 += 1
            tr1 = tr1.next
            
        c2 = 0
        tr2 = h2
        while tr2 != None:
            c2 += 1
            tr2 = tr2.next
        
        if c1 > c2:
            for i in range(c1-c2):
                h1 = h1.next
        else:
            for i in range(c2-c1):
                h2 = h2.next
        
        while h1 != None and h1 != h2:
            h1 = h1.next
            h2 = h2.next
        
        print ("Loop starts :: ", h1.data)
        
        
o = LinkedList([1,4,2,8,5,9,7,56])

#print (list(range(9-1)))
o.append(99, 0)
o.append(75, 0)
o.append(66, 0)
o.append(45, 0)
o.append(23, 0)
o.append(3, 0)

print (o, o.head.data, o.tail.data)

#o.remove(2)

#print (o, o.head.data, o.tail.data)

o.findNthElementFromLast(9)

o.findNthElementfromEnd(9)

o.findMiddleElement()

#o.reverseLinkedList()
#print (o, o.head.data, o.tail.data)

o.isListLoop()

