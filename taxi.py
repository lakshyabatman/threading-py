import threading
from queue import Queue
import time
import datetime

f=open("myTaxiLog.txt","w+")

def start_service(number_of_passengers,number_of_cabs):

    print_lock = threading.Lock()
    def ride(passenger):
        time.sleep(2) 
        with print_lock:
            log="Ride : Cab ID:"+str(threading.current_thread().name) + " Passenger Number: " +str(passenger)+" Ride started at "+ str( datetime.datetime.now())+"\n"
            print(log)
            f.write(log)
    def threader():
        while True:
            worker = q.get()
            ride(worker)
            q.task_done()

    q = Queue()

    for x in range(number_of_cabs):
        t = threading.Thread(target=threader)
        t.daemon = True
        t.start()

    start = time.time()

    for passenger in range(number_of_passengers):
        q.put(passenger)

    q.join()

    print('Entire job took:',time.time() - start)
    print("If we haven't use threading then it would take", number_of_passengers*2)

print("                        Welcome To TAXI SERVICE                  ")
print("This Project stimulates a How Multithreading can save lot of compututional time!")
print("We used Threading Library for adding threads and locks")
print("""
    1. Lakshya Khera : 9917103014
    2. Gaurav Singh Parihar : 9917103015
    3. Shubham Tak : 9917103031
""")
number_of_passengers=int(input("Write number of passengers!!:"))
number_of_cabs=int(input("We need Cabs!:TELL ME Number of Cabs:"))
start_service(number_of_passengers=number_of_passengers,number_of_cabs=number_of_cabs)

print("Happiness is to have all data displayed on the terminal is getting saved in a log file :)")
print("                 Made in Love with Python and Linux <3            ")
f.close()