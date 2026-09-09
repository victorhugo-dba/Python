# multithreading = used to perform multiple tasks concurrently (multitasking)
#                  good for I/O bound tasks like reading files or fetching data frfom APIs
#                  threading.thread(target=my_function)

import threading
import time

def walk_dog():
    time.sleep(8)
    print("You finish walking the dog")

def take_out_trash():
    time.sleep(2)
    print("you take out the trash")

def get_the_mail():
    time.sleep(4)
    print("You get the mail")

# walk_dog()
# take_out_trash()
# get_the_mail()

chore1 = threading.Thread(target=walk_dog)
chore1.start()

chore2 = threading.Thread(target=take_out_trash)
chore2.start()

chore3 = threading.Thread(target=get_the_mail)
chore3.start()

chore1.join()
chore2.join()
chore3.join()

print("all chores are complete!")