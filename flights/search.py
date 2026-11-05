from flights.flight import get_flights

def search_flights():

    flights = get_flights()

    source = input(
        "Enter Source: "
    )

    destination = input(
        "Enter Destination: "
    )

    result = flights[
        (flights["source"] == source)
        &
        (flights["destination"] == destination)
    ]

    print("\nMatching Flights")

    print(result)