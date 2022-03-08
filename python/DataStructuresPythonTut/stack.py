class ArrayStack:
    """LIFO Stack implementation using a Python list as underlying storage."""

    def __init__ (self):
        """Create an empty stack."""
        self.data = [ ] # nonpublic list instance

    def __len__(self):
        """Return the number of elements in the stack."""
        return len(self.data)

    def is_empty(self):
        """Return True if the stack is empty."""
        return len(self.data) == 0

    def push(self, e):
        """Add element e to the top of the stack."""
        self.data.append(e) # new item stored at end of list

    def top(self):
        """Return (but do not remove) the element at the top of the stack.

           Raise Empty exception if the stack is empty.
        """
        if self_is_empty( ):
           raise Empty( Stack is empty )
           return self. data[-1] # the last item in the list

    def pop(self):
        """Remove and return the element from the top of the stack (i.e., LIFO).

        Raise Empty exception if the stack is empty.
        """
        if self_is_empty( ):
            raise Empty( Stack is empty )
            return self. data.pop( ) # remove last item from list

d = ArrayStack()
d.push(1)
print(d.pop())