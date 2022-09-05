class Queue :

    def __init__(self, items = None) :
        if items == None or items == [] :
            self.items = []
        else :
            self.items = items

    def enQueue(self, i) :
        self.items.append(i) #insert ท้าย list

    def deQueue(self) :
        return self.items.pop(0) #pop ตัวหน้าสุดของ list

    def insert(self,n,i) :
        self.items.insert(n,i) #insert ตามตำแหน่งที่ต้องการ

    def isEmpty(self) :
        return self.items == []

    def size(self) :
        return len(self.items)

inp , hint = input('Enter code,hint : ').split(',')
code = Queue()
n = ord(hint) - ord(inp[0])
#add hint
code.enQueue(hint)
print(code.items)
#dequeue first queue
for i in range(1,len(inp)) :
    code.enQueue(chr(ord(inp[i])+n))
    print(code.items)



