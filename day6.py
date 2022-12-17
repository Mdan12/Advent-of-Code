text_file = 'day6.txt'
skra = open(text_file, 'r').read()
length = len(skra)
i=0
sum=4
j=0
mylist = []
while i<4:
    mylist.append(skra[i])
    i+=1

while j<length-4:
    res = len([*set(mylist)])
    if res != 4:
        sum+=1
        mylist.pop(0)
        mylist.append(skra[i])
        i+=1
        j+=1
    if res == 4:
        print(sum)
        sum = 14
        i = 0
        j = 0
        mylist.clear()
        break

while i<14:
    mylist.append(skra[i])
    i+=1

while j<length-14:
    res = len([*set(mylist)])
    if res != 14:
        sum+=1
        mylist.pop(0)
        mylist.append(skra[i])
        i+=1
        j+=1
    if res == 14:
        print(sum)
        break
    
