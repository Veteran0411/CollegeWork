count=1000
packets=[500,450,400,300,600,200,400]

index=len(packets)-1
while(index>=0):
    while(count>packets[index]):
        count-=packets[index]
        print(f"packet movie out of the queue := {packets[index]}")
        index-=1
        if index<0:
            exit
    print(f"count is less than packet size ")
    count=1000