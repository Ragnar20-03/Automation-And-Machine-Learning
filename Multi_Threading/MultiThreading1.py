
import os 
import threading

def Task1(Value):
    print("PID of Task 1 is : " , os.getpid())
    print("Thread id of Task1 Thread is : " , threading.get_ident())
    print()


def Task2(Value):
    print("PID of Task 2 is : " , os.getpid())
    print("Thread id of Task2 Thread is : " , threading.get_ident())
    print()


def main(): 
    print("Inside Main")
    print()
    print("PID of Parent of Thread Process is : " , os.getpid())
    print("Thread id of Main Thread is : " , threading.get_ident())

    print()

    No = 5
    t1 = threading.Thread(target= Task1 , args = (No ,)  )
    t2 = threading.Thread(target= Task2 , args = (No ,)  )

    print(t1)  # -> object
    print()
    t1.start()
    t2.start() 
     
    t2.join() 
    t1.join()

if __name__=="__main__" :
    main()