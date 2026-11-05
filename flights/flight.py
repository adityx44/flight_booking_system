import pandas as pd

def get_flights():

    return pd.read_csv(
        "data/flights.csv"
    )

def show_flights():

    flights = get_flights()

    print("\nAvailable Flights")
    print(flights)