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

    def insert(self,i) :
        self.items.insert(0,i)

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
q = Queue()
for c in data :
    if c == 'E' :
        pass
    elif c == 'D' :
        if q.isEmpty() :
            print(-1)
        else :
            print(str(q.deQueue()) + ' 0')
    else :
        q.enQueue(c)
        print(q.size())
if q.isEmpty() :
    print("Empty")
else :
    for item in q.items :
        print(item, end = " ")