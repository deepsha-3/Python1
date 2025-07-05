# Write a class Bus which has methods to book a ticket, get status(no of sets) and get fare infomation of Bus running under Nepal Highway Authority.

import random
class Bus:
    def __init__(self, busNo):
        self.busNo =busNo

    def book(self, busNo, lofrom, to):
        print(f"Ticket is booked in bus no: {busNo} from {lofrom} to {to}")

    def getStatus(self, busNo):
        print("The bus is going on the road.")

    def getFare(self, busNo, lofrom, to ):
        print(f"Ticket is fare in bus no: {busNo} from {lofrom} to {to} is {random.randint(1, 222)}")

bus = Bus(3450) 
bus.book( 3450, "Waling", "Kathmandu")
bus.getStatus(3450)
bus.getFare(3450, "Waling", "Kathmandu")