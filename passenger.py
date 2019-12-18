import threading
import message


class Passenger(object):
    PASSENGER_NUMBER = 1
    def __init__(self, taxis: list):
        self.number = Passenger.PASSENGER_NUMBER
        self.msg = message.Message()
        self.taxis = taxis
        self.is_take = False
        self.thread = threading.Thread(target=self.run)
        self.can_die = False
        self.msg.enterMuseum(self.number)
        Passenger.PASSENGER_NUMBER += 1
    
    def run(self):
        self.msg.waitingForTaxi(self.number)
        while not self.can_die:
            for taxi in self.taxis:
                if not self.is_take and taxi.can_take_me():
                    self.is_take = True
                    self.msg.enterTaxi(self.number, taxi.number)
                    taxi.take(self)
                elif self.can_die:
                    break
    
    def start(self):
        self.thread.start()
        
    def die(self, taxi):
        self.can_die = True
