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

def Activity(code) :
    if code == '0' :
        return 'Eat:'
    elif code == '1' :
        return 'Game:'
    elif code == '2' :
        return 'Learn:'
    elif code == '3' :
        return 'Movie:'

def Location(code) :
    if code == '0' :
        return 'Res.'
    elif code == '1' :
        return 'ClassR.'
    elif code == '2' :
        return 'SuperM.'
    elif code == '3' :
        return 'Home'

def manage_score(activity,location) :
    score = 0
    if activity == True and location == False :
        score = 1
    elif activity == False and location == True :
        score = 2
    elif activity == True and location == True :
        score = 4
    elif activity == False and location == False :
        score = -5
    return score
#input
## Activity : Location
## my your , my your
##Activity 0:Eat 1:Game 2:Learn 3:Movie
##Location 0:Res. 1:ClassR. 2:SuperM. 3:Home
inp = input("Enter Input : ").split(',')
my_queue = Queue()
your_queue = Queue()

score = 0
for item in inp :
    m,y = item.split(' ')
    my_queue.enQueue(m)
    your_queue.enQueue(y)
#output
print("My   Queue = " + ', '.join(my_queue.items))
print("Your Queue = " + ', '.join(your_queue.items))
for i in range(my_queue.size()) :
    my_string = ""
    your_string = ""
    state = 0 #activity = 0 location = 1
    activity = False
    location = False 
    for j in range(len(my_queue.items[i])) :
        my = my_queue.items[i][j]
        your = your_queue.items[i][j]
        if my and your == ":":
            state += 1
        else :
            if state == 0 : #activity
                if my == your : #activity เหมือนกัน
                    activity = True
                    my_string += Activity(my_queue.items[i][j])
                    your_string += Activity(your_queue.items[i][j])
                else :
                    activity = False
                    my_string += Activity(my_queue.items[i][j])
                    your_string += Activity(your_queue.items[i][j])
            else : #location
                if my == your : #location เหมือนกัน
                    location = True
                    my_string += str(Location(my_queue.items[i][j]))
                    your_string += Location(your_queue.items[i][j])
                else :
                    location = False
                    my_string += Location(my_queue.items[i][j])
                    your_string += Location(your_queue.items[i][j])
    score += manage_score(activity,location)
    my_queue.items[i] = my_string
    your_queue.items[i] = your_string

print("My   Activity:Location = " + ', '.join(my_queue.items))
print("Your Activity:Location = " + ', '.join(your_queue.items))
#score 
if score >= 7 :
    print("Yes! You're my love! : Score is " + str(score) + '.')
elif score < 7 and score > 0 :
    print("Umm.. It's complicated relationship! : Score is " + str(score) + '.')
else :
    print("No! We're just friends. : Score is " + str(score) + '.')


