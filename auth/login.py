import pandas as pd

def login():

    users = pd.read_csv(
        "data/users.csv"
    )

    username = input("Username: ")
    password = input("Password: ")

    user = users[
        (users["username"] == username)
        &
        (users["password"] == password)
    ]

    if len(user) > 0:

        print("Login Successful")

        return int(
            user.iloc[0]["user_id"]
        )

    print("Invalid Login")

    return None