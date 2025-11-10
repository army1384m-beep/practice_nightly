import time
from datetime import datetime
import colorama
from colorama import Fore, Back, Style, init

init()

class Report:
    def __init__(self, filename):
        self.filename = filename


    def __enter__(self):
        self.file = open( self.filename, 'a')
        return self.file
    

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()

    
    
class Machine:
    counter = 0   
    def __init__(self, name):
        self.status = 'stand by'
        self.name = name 

    def start(self):
        try:
            if self.status == 'stand by':
                self.status = 'active'
                self.time = datetime.now().strftime('%H :%M : %S')
                Machine.counter += 1
                print(Fore.GREEN + "machine activated!")
            else :
                raise ValueError

        except: 
            print("machine is already active")

        return f"{self.status}:{self.time}: {self.name}\n"
    

    def pause(self):
        try:
            if self.status == 'active':
                self.status = 'pause'
                self.time = datetime.now().strftime('%H :%M : %S')
                Machine.counter += 1
                print(Fore.BLUE + "machine paused!")

            else :
                raise ValueError

        except: 
            print("machine is already paused")

        return f"{self.status}:{self.time}: {self.name}\n"


    def finish(self):
        try:
            if self.status != 'active' and self.status !='pause':
                self.status = 'finish'
                self.time = datetime.now().strftime('%H :%M : %S')
                Machine.counter += 1
                print(Fore.YELLOW + "machine finishied!")

            else :
                raise ValueError

        except: 
            print("machine is already finish")

        return f"{self.status}:{self.time}: {self.name}\n "



    def recharge():
        def gen():
            for i in range(10, 101, 10):
                time.sleep(1)
                yield f"is charging in level: {i}"

        for i in gen():
            print(i)

    recharge()




        

m1 = Machine('akbar')
m2 = Machine('asghar')

with Report('text.txt') as rp:
    rp.write(m1.start())
    rp.write(m2.start())
    rp.write(m1.pause())
    rp.write(m2.finish())
    

#print(m1.recharge())




    # m1 = Machine('akbar')
    # m1.start()



# rp.write(self.time)
# m1 = Machine()


            
