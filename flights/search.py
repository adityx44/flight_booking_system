from flights.flight import get_flights

def search_flights():
    flights = get_flights()

    source = input("Source: ")
    destination = input("Destination: ")

    result = flights[
        (flights["source"] == source) &
        (flights["destination"] == destination)
    ]

    print(result)