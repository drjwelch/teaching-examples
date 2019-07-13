# Insertion sort - WITH ERROR

def slidelist(mylist,position,value):
    slide_pos = position-1
    while mylist[slide_pos]>value and slide_pos<=0:
        mylist[slide_pos+1] = mylist[slide_pos]
        slide_pos = slide_pos - 1
    return slide_pos+1

def insort(mylist):
    for i in range(1,len(mylist)):
        temp = mylist[i]
        gap_position = slidelist(mylist,i,temp)
        mylist[gap_position] = temp
        print("Next step: ",mylist)

# Main program

list = [8,2,7,1,0,3,5,4,9,6]

print("Insertion sort")
print("==============")
print
print("Starting list  : ", list)

insort(list)

print("Sorted list  : ", list)
