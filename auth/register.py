import pandas as pd

def register():

    users = pd.read_csv("data/users.csv")

    username = input("Username: ")
    password = input("Password: ")

    user_id = len(users) + 1

    new_user = pd.DataFrame({
        "user_id":[user_id],
        "username":[username],
        "password":[password]
    })

    users = pd.concat(
        [users,new_user],
        ignore_index=True
    )

    users.to_csv(
        "data/users.csv",
        index=False
    )

    print("Registration Successful")