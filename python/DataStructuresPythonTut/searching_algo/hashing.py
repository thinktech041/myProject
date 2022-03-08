# IMPLEMENTING A HASH TABLE FOR TWO LISTS IN PYTHON
# Below we use two lists to create a HashTable class that
# Implements the Map abstract data
# type. One list, called slots, will hold the 
# key items and a parallel list, called data, will hold
# the data values. 

# hash_function implements the simple remainder method. The collision resolution
#  technique is linear probing with a “plus 1” rehash function.
#  The put function assumes that there will eventually be an empty slot unless 
# the key is already present in the self.slots. 
# It computes the original hash value and if that slot is not empty,
#  iterates the rehash function until an empty slot occurs. 
# If a nonempty slot already contains the key, 
# the old data value is replaced with the new data value.




class HashTable:
    
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
    
    def hash_function(self, key, size):
        # IT IMPLEMENTS THE REMAINDER HASH FUNCTION METHOD
        return key % size

    def rehash(self, old_hash, size):
        # IT IMPLIMENTS THE LINEAR PROBING METHOD WITH A PLUS 1 REHASH FUNCTION
        return (old_hash + 1) % size

    def put(self, key,value):
        #  put(key,val) Add a new key-value pair to the map.
        #  If the key is already in the map
        #  then replace the old value with the new value.

        hash_value = self.hash_function(key,len(self.slots))
        if self.slots[hash_value] == None:
            self.slots[hash_value] = key
            self.data[hash_value] = data
        else:
            if self.slot[hash_value] == key:
                self.data[hash_value] = data #replace
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] != None and self.slots[next_slot] != key:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] == None:
                    self.slots[next_slot] = key
                    self.data[next_slot] = data
                else:
                    self.data[next_slot] = data #replace
    
    def get(self, key):
        # get(key) Given a key, return the value 
        # stored in the map or None otherwise.

        start_slot = self.hash_function(key, len(self.slots))
        data = None
        stop = False
        found = False
        position = start_slot
        while self.slots[position] != None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position=self.rehash(position, len(self.slots))
                if position == start_slot:
                    stop = True
        return data

    def __getitem__(self, key):
        return self.get(key)
    
    def __setitem__(self, key, data):
        return self.put(key, data)
