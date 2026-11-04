class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Fila:
    def __init__(self):
        self.fila = []
    def insert(self,item):
        return self.fila.append(item)
    def remove(self):
        out = self.fila[0]
        del self.fila[0]
        return out
    def list(self):
        return self.fila
