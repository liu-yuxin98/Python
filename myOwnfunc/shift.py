def left_move(list):
    temp=list[0]
    for i in range(0,len(list)-1):
        list[i]=list[i+1]
    list[-1]=temp

def right_move(list):
    i=len(list)-1
    temp=list[i]
    while i > 0:
        list[i]=list[i-1]
        i=i-1
    list[0]=temp






