import pandas as pd

def total_bookings():

    try:

        bookings = pd.read_csv(
            "data/bookings.csv"
        )

        print(
            "Total Bookings:",
            len(bookings)
        )

    except:

        print(
            "No Bookings Available"
        )