import random
from passenger import Passenger
import threading
import time
import message


class Taxi(object):
    TAXI_NUMBER = 1
    def __init__(self, livein_muesum: int = random.randint(1, 5), capacity: int = 1):
        self.passengers = []
        self.thread = threading.Thread(target=self.run)
        self.sem = threading.Semaphore(capacity)
        self.cap = capacity
        self.number = Taxi.TAXI_NUMBER
        self.lock = threading.Lock()
        self.livein_muesum = livein_muesum
        Taxi.TAXI_NUMBER += 1
        self.msg = message.Message() 
    
    def take(self, passenger: Passenger):
        self.sem.acquire()
        self.passengers.append(passenger)
    
    def run(self):
        while True:
            while self.sem._value > 0:
                pass
            
            self.msg.inTaxi(self.number)
            time.sleep(self.livein_muesum)
            self.passengers.clear()
            for _ in range(self.cap):
                self.sem.release()
            self.msg.exitTaxi(self.number)
                
            

    def can_take_me(self):
        self.lock.acquire()
        result = self.sem._value != 0
        self.lock.release()
        return result
    
    def start(self):
        self.thread.start()
