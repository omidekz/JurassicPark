import threading


class Message:
    msg = None
    def __new__(cls):
        if Message.msg:
            return Message.msg
        Message.msg = Message.__Message()
        return Message.msg
    
    class __Message:
        def __init__(self):
            self.lock = threading.Lock()

        def enterMuseum(self, numThread):
            self.lock.acquire()
            print (numThread , "enter Museum 🚶")
            self.lock.release()

        def waitingForTaxi(self, numThread):
            self.lock.acquire()
            print(numThread , "waiting for taxi 🕐")
            self.lock.release()

        def enterTaxi(self, numThread, numTaxi):
            self.lock.acquire()
            print(numThread , "enter to taxi" , numTaxi, '🏃')
            self.lock.release()

        def inTaxi(self,numTaxi):
            self.lock.acquire()
            print("\t", numTaxi , "started 🚕")
            self.lock.release()

        def exitTaxi(self, numTaxi):
            self.lock.acquire()
            print("\t", numTaxi, "stopped 🚏")
            self.lock.release()



