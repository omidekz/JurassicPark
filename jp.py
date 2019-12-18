import passenger
import taxi
import random


def main(taxi_number: int, passenger_number: int, capacity: int = 1):
    print('{} taxi exist in museum with {} capacity, and there are {} people'.format(taxi_number, capacity, passenger_number))
    
    taxis = [taxi.Taxi(capacity=capacity) for _ in range(taxi_number)]
    random.shuffle(taxis)
    
    passengers = [passenger.Passenger(taxis) for _ in range(passenger_number)]
    random.shuffle(passengers)
    
    for tx in taxis:
        tx.start()
    for ps in passengers:
        ps.start()

main(3, 8, 2)
