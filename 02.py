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
        self.items.insert(n,i)

    def isEmpty(self) :
        return self.items == []

    def size(self) :
        return len(self.items)

def str_to_list(inp) :
    l = []
    x = ""
    n = 0
    while n < len(inp) :
        if inp[n] == ',' or inp[n] == " " :
            if x.isnumeric() :
                l.append(int(x))
            else :
                l.append(x)
            x = ""
        else :
            x += inp[n]
        n += 1
    if x.isnumeric() :
        l.append(int(x))
    elif not x.isnumeric() :
        try :
            l.append(int(x))
        except :
            l.append(x)
    return l

#main#
inp = input("Enter Input : ")
data = str_to_list(inp)
status = Queue()
q = Queue()
n = 0
for c in data :
    if c == 'EN' :
        status.enQueue(c)
    elif c == 'ES' :
        status.enQueue(c)
    elif c == 'D' :
        if q.isEmpty() :
            print('Empty')
        else :
            if n != 0 :
                n -= 1
            print(q.deQueue())
    else :
        if status.items[-1] == 'EN' :
            status.deQueue()
            q.enQueue(c)
        elif status.items[-1] == 'ES' :
            status.deQueue()
            q.insert(n,c)
            n += 1

        
