#multithreading = performing several task at once 
# threading.Thread(target = , args= ) tar,arg keywords 


import threading
import time 

def centre():
    time.sleep(5)
    print("Teachers")

def room():
    time.sleep(3)
    print("Exams ")

def papers(name):
    time.sleep(3)
    print(f"Chekcing {name}")

seq1 = threading.Thread(target= centre)
seq1.start()

seq2=threading.Thread(target=room)
seq2.start()

seq3=threading.Thread(target=papers, args=("MATH" ,))   #since the one parameter in tuple gotta end with comma 
seq3.start()


