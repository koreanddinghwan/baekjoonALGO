class stack:
    def __init__(self):
        self.items = []
        
    def push(self, val):
        self.items.append(val)
        
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("empty stack")
            
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("empty stack")
            
    def __len__(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self) == 0