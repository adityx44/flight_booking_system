import pandas as pd

def book_flight(user_id):

    flight_id = int(
        input("Flight ID: ")
    )

    booking = pd.DataFrame({
        "user_id":[user_id],
        "flight_id":[flight_id]
    })

    try:

        old = pd.read_csv(
            "data/bookings.csv"
        )

        booking = pd.concat(
            [old, booking],
            ignore_index=True
        )

    except:
        pass

    booking.to_csv(
        "data/bookings.csv",
        index=False
    )

    print("Flight Booked")