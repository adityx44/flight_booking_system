import pandas as pd

def booking_history(user_id):

    bookings = pd.read_csv(
        "data/bookings.csv"
    )

    history = bookings[
        bookings["user_id"] == user_id
    ]

    print(history)