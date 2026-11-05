from auth.register import register
from auth.login import login

from flights.flight import show_flights
from flights.search import search_flights


from analytics.analytics import total_bookings

while True:

    print("\n===== FLIGHT BOOKING SYSTEM =====")

    print("1 Register")
    print("2 Login")
    print("3 Exit")

    choice = input("Choice: ")

    if choice == "1":

        register()

    elif choice == "2":

        user_id = login()

        if user_id:

            while True:

                print("\n1 View Flights")
                print("2 Search Flights")
                print("3 Book Flight")
                print("4 Analytics")
                print("5 Logout")

                option = input("Option: ")

                if option == "1":

                    show_flights()

                elif option == "2":

                    search_flights()

                elif option == "3":

                    book_flight(user_id)

                elif option == "4":

                    total_bookings()

                elif option == "5":

                    break

    elif choice == "3":

        break