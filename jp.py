import passenger
import taxi


def main(taxi_number: int, passenger_number: int, capacity: int = 1):
    print('{} taxi exist in museum with {} capacity, and there are {} people'.format(taxi_number, capacity, passenger_number))
    taxis = [taxi.Taxi(capacity=capacity) for _ in range(taxi_number)]
    for tx in taxis:
        tx.start()

    for _ in range(passenger_number):
        passenger.Passenger(taxis).start()

main(3, 8, 2)
