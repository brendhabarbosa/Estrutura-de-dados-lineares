class Deque:
    def __init__(self):
        self.deque = []
    def insert_front(self, item):
        self.deque.insert(0,item)
        return self.deque
    def insert_back(self,item):
        self.deque.append(item)
    def remove_front(self):
        if self.is_empty():
            print("Deque vazio") 
        front = self.deque[0]
        del self.deque[0]
        return front
    def remove_back(self):
        if self.is_empty():
            print("Deque vazio")
        back = self.deque[-1]
        del self.deque[-1]
        return back
    def list(self):
        return self.deque
    def list_reverse(self):
        self.deque[::-1]
        return self.deque
    def is_empty(self):
        return len(self.deque) == 0

