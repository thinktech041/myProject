class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None # this prev is implemented only in doubly linked list

    def get_prev(self):
        return self.prev

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data
    
    def set_prev(self,new):
       self.prev = new

    def set_next(self,new):
       self.next = new

    def set_data(self,new):
       self.data = new


class unordList:
    def __init__(self,head):
        self.head = None

    def is_empty(self):
        return self.head == None

    def add(self, item):
        store = Node(item)
        store.set_next(self.head)
        self.head = store
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count+=1
            current = current.get_next()
        return count

    def search(self,item):
        current=self.head
        found = False
        while current != None and not found:
            if current.get_data()==item:
                found = True
            else:
                current= current.get_next()
        return found
    
    def delete(self,item):
        current=self.head
        previous=None
        found=None
        while  not Found:
            if current.get_data()== item:
                found=True
            else:
                previous=current
                current=current.get_next()

        if previous==None:
            self.head=self.head.get_next()
        else:
            previous.next=current.get_next()

    def rev_Singly_Linklist(self):
        # the reverse of the linked list is implemented using a temporary
        # value to store the previous node in the network
        current = self.head
        previous = None
        #the while loop help's to traverse through all the node
        while current!= None:
            previous = current
            current = current.get_next()
            current.next = current

        
        




            




            

        
        
        