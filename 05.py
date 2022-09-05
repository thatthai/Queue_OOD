##Queue
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

##Stack
class Stack :
    def __init__(self,items = None) :
        if items == [] or items == None :
            self.items = []
        else :
            self.items = items

    def push(self,i) :
        self.items.append(i)

    def pop(self) :
        return self.items.pop(-1)

    def size(self) :
        return len(self.items)

    def isEmpty(self) :
        return self.items == []

normal,mirror = input('Enter Input (Normal, Mirror) : ').split(' ')
#การขัดกันของระเบิดจะเกิดขึ้นฝนลูกที่ 2 กับลูกที่ 3
#หาระเบิกฝั่งโลกกระจกก่อนแล้วเอามาเก็บใน stack
expolse_count = 0
explose = 0
failed = 0
finish = 0
mirror_explose = 0
mirror_stack = Stack()
mirror_explose_stack = Stack()
normal_stack = Stack()
normal_queue = Queue()

#mirror check explosion
for c in mirror[::-1] :
    if mirror_stack.isEmpty() :
        mirror_stack.push(c)
    else :
        if c == mirror_stack.items[-1] :
            expolse_count += 1
            mirror_stack.push(c)
        else :
            expolse_count = 0
            mirror_stack.push(c)
    if expolse_count == 2 :
        mirror_explose_stack.push(mirror_stack.pop())
        mirror_stack.pop()
        mirror_stack.pop()
        expolse_count = 0
##case ถ้าเกิดเหลือตัวสุดท้ายแล้วนับ explose count ได้ไม่ครบจนมันไม่ถูดระเบิดทั้ง ๆ ที่ควรระเบิด (เก็บตก) 
if mirror_stack.size() == 3 :
    if mirror_stack.items[0] == mirror_stack.items[1] == mirror_stack.items[2] :
        mirror_explose_stack.push(mirror_stack.pop())
        mirror_stack.pop()
        mirror_stack.pop()
mirror_explose = mirror_explose_stack.size()

mirror_explose_stack.items = mirror_explose_stack.items[::-1]
expolse_count = 0
#add item to normal
for c in normal :
    if normal_queue.isEmpty() :
        normal_queue.enQueue(c)
    else :
        if c == normal_queue.items[-1] :
            expolse_count += 1
            normal_queue.enQueue(c)
        else :
            expolse_count = 0
            normal_queue.enQueue(c)
    if expolse_count == 2 :
        
        if not mirror_explose_stack.isEmpty() :
            if mirror_explose_stack.items[-1] == c :
                failed += 1
            else :
                finish += 1
            normal_queue.insert(normal_queue.size()-1,mirror_explose_stack.pop())
        expolse_count = 0

expolse_count = 0
#explose normal
for c in normal_queue.items :
    if normal_stack.isEmpty() :
        normal_stack.push(c)
    else :
        if c == normal_stack.items[-1] :
            expolse_count += 1
            normal_stack.push(c)
        else :
            expolse_count = 0
            normal_stack.push(c)
    if expolse_count == 2 :
        explose += 1
        normal_stack.pop()
        normal_stack.pop()
        normal_stack.pop()
        expolse_count = 0

#setup value of result
normal = ''.join(normal_stack.items)
mirror = ''.join(mirror_stack.items)

#output
print("NORMAL :")
if normal_stack.size() == 0 :
    print(normal_stack.size())
    print("Empty")
else :
    print(normal_stack.size())
    print(normal[::-1])
print(str(explose - failed) + " Explosive(s) ! ! ! (NORMAL)")
if failed != 0 :
    print("Failed Interrupted " + str(failed) + " Bomb(s)")
print("------------MIRROR------------")
print(": RORRIM")
if mirror_stack.size() == 0 :
    print(mirror_stack.size())
    print("ytpmE")
else :
    print(mirror_stack.size())
    print(mirror[::-1])
print("(RORRIM) ! ! ! (s)evisolpxE " + str(mirror_explose))
