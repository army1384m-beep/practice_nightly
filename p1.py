from datetime import datetime

class Report:
    def __init__(self, filename):
        self.filename = filename


    def __enter__(self):
        self.file = open( self.filename, 'a')
        return self.file
    

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.file.close()

    
    
class Machine:   
    def __init__(self, name):
        self.status = 'stand by'
        self.name = name 

    def start(self):
        try:
            if self.status == 'stand by':
                self.status = 'active'
                self.time = datetime.now().strftime('%H :%M : %S')

            else :
                raise ValueError

        except: 
            print("machine is already active")

        return f"{self.status}:{self.time}:"
    
    

m1 = Machine('akbar')

with Report('text.txt') as rp:
    rp.write(m1.start())

    # m1 = Machine('akbar')
    # m1.start()



# rp.write(self.time)
# m1 = Machine()


            
