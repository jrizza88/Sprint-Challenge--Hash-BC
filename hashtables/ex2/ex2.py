#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_retrieve
)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    hashtable = HashTable(length)
    route = [None] * length

    """
    YOUR CODE HERE
    """
    for i in range(0, length):
        hash_table_insert(hashtable, tickets[i].source, tickets[i].destination)
        print('tickets[i].destination: ', tickets[i].destination)
        print('tickets[i].source: ', tickets[i].source)

        #source = "NONE"
        route[0] = hash_table_retrieve(hashtable, "NONE")
        print('route: ', route)
    for i in range(1, length):
        temp_route = hash_table_retrieve(hashtable, route[i - 1])
        print('temp_route', temp_route)
        route[i] = temp_route

    print("final route", route)
    return route
