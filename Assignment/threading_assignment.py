import datetime
from threading import Thread 
# count 1 billion numbers
#thread_op = []
numlist = []
def counter1(threadID,n1,n2):
    num = n1 - 1
    for c in range(n1,n2+1):
        num = num+1
        numlist.append(num)
    #thread_op.append({"threadID":threadID,"num":numlist})

# counter1(1,250000001)
# counter1(250000001,500000001)
# counter1(500000001,750000001)
# counter1(750000001,1000000001)

print("Start Time ", datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))

# Create a Thread Object using the Thread class of the threading module
t1 = Thread(target=counter1, args=(1,1,250000000,))
t1.start()
t1.join()

# Create one more Thread Object using the Thread class of the threading module
t2 = Thread(target=counter1, args=(2,250000001,500000000,))
t2.start()
t2.join()

# Create a Thread Object using the Thread class of the threading module
t3 = Thread(target=counter1, args=(3,500000001,750000000,))
t3.start()
t3.join()

# Create one more Thread Object using the Thread class of the threading module
t4 = Thread(target=counter1, args=(4,750000001,1000000000,))
t4.start()
t4.join()

"""
t1 = Thread(target=counter1, args=(1,1,25,))
t1.start()
t1.join()

# Create one more Thread Object using the Thread class of the threading module
t2 = Thread(target=counter1, args=(2,26,50,))
t2.start()
t2.join()

# Create a Thread Object using the Thread class of the threading module
t3 = Thread(target=counter1, args=(3,51,75,))
t3.start()
t3.join()

# Create one more Thread Object using the Thread class of the threading module
t4 = Thread(target=counter1, args=(4,76,100,))
t4.start()
t4.join()
"""
print("End Time ", datetime.datetime.today().strftime("%d-%b-%Y %H:%M:%S"))

print(numlist)