from multiprocessing import Process, \
  BoundedSemaphore, Semaphore, Lock, Condition,\
  current_process, \
  Value, Array, Manager

class Table():
    def __init__(self,NPHIL,manager):
        self.current_phil = None 
        self.phil = manager.list([False]*NPHIL)
        self.neating = Value('i',0)
        self.mutex = Lock()
        self.freefork = Condition(self.mutex)

    def no_comen_lados(self):
        return(self.phil[(self.current_phil+1)%len(self.phil)]==False and self.phil[(self.current_phil-1)%len(self.phil)]==False)
        
    def wants_eat(self,i):
        self.mutex.acquire()
        self.freefork.wait_for(self.no_comen_lados)
        self.phil[i] = True
        self.neating.value+=1
        self.mutex.release()
        
    def set_current_phil(self,i):
        self.current_phil = i
        
    def wants_think(self,i):
        self.mutex.acquire()
        self.phil[i] = False
        self.neating.value-=1
        self.freefork.notify_all()
        self.mutex.release()
        
    def __str__(self):
        return f"M<r:{self.nread.value}, w:{self.nwrite.value}>"
    
class CheatMonitor():
    def __init__(self):

        self.mutex = Lock()
        self.other = Condition(self.mutex)
        self.neating = Value('i',0)
        
    def is_eating(self,N):
        
        self.neating.value+=1
        self.other.acquire()


    def wants_think(self,N):

        self.other.release()
        self.neating.value-=1

    def __str__(self):
        return f"M<r:{self.nread.value}, w:{self.nwrite.value}>"
    