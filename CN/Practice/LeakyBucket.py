from time import sleep
count=1000
packets=[400,300,700,350,600]

index=len(packets)-1

while index>=0:
    while count>packets[index]:
        count-=packets[index]
        print(f"sent packet from queue: {packets[index]}")
        sleep(1)
        index-=1
        if index<0:
            print("all the packets sent")
            exit
    print("restored the count capacity")
    count=1000
