class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):        
        result = 0
        for i in range(len(value)):
            result += (ord(value[i]) * (1+i))
        result = result % self.size
        return result
    
    def seek_slot(self, value):
        slot_number = self.hash_fun(value)
        if self.slots[slot_number] is None:
            return slot_number
        else:
            for i in range(self.size):
                slot_number += self.step
                if slot_number >= self.size:
                    slot_number -= self.size
                if self.slots[slot_number] is None:
                    return slot_number
        return None

    def put(self, value):
        slot_number = self.seek_slot(value)
        if slot_number is not None:
            self.slots[slot_number] = value
            return slot_number
        else:
            return None

    def find(self, value):
        slot_number = self.hash_fun(value)
        if self.slots[slot_number] == value:
            return slot_number
        else:
            for i in range(self.size):
                slot_number += self.step
                if slot_number >= self.size:
                    slot_number -= self.size
                if self.slots[slot_number] == value:
                    return slot_number
        return None
