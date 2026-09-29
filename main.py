#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
import requests_cache
from datetime import datetime, timedelta
from pprint import pprint
from data_manager import DataManager
from flight_search import FlightSearch
from flight_data import find_cheapest_flight
from notification_manager import NotificationManager

notification_manager = NotificationManager()

ORIGIN_CITY_IATA = "IDR"

requests_cache.install_cache(
    "flight_cache",
    urls_expire_after={
        "*.sheety.co*": requests_cache.DO_NOT_CACHE,
        "*": 3600,
    }
)

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()
customers_emails = data_manager.get_customers_emails()
customers_email_list = [row["enterYourEmailAddress"] for row in customers_emails]

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6 * 30))

flight_search = FlightSearch()

flights = flight_search.check_flights(
    origin_city_code = "IDR",
    destination_city_code = "HND",
    from_time = tomorrow,
    to_time = six_month_from_today,
)

for destination in sheet_data:
    pprint(f"checking flight for {destination['city']}.......")
    flights = flight_search.check_flights(
    ORIGIN_CITY_IATA,
    destination['iataCode'],
    from_time = tomorrow,
    to_time = six_month_from_today,
    )

    cheapest_flight = find_cheapest_flight(flights, return_date=six_month_from_today.strftime("%Y-%m-%d"))
    pprint(f"{destination['city']}: INR {cheapest_flight.price}")

    if cheapest_flight.price != "N/A" and cheapest_flight.price < destination["lowestPrice"]:
        # Customise the message depending on the number of stops
        if cheapest_flight.stops == 0:
            message = f"Low price alert! Only ₹ {cheapest_flight.price} to fly direct " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"on {cheapest_flight.out_date} until {cheapest_flight.return_date}."
        else:
            message = f"Low price alert! Only ₹ {cheapest_flight.price} to fly " \
                      f"from {cheapest_flight.origin_airport} to {cheapest_flight.destination_airport}, " \
                      f"with {cheapest_flight.stops} stop(s) " \
                      f"departing on {cheapest_flight.out_date} and returning on {cheapest_flight.return_date}."


        notification_manager.send_whatsapp(message_body=message)

        print(f"Check your email. Lower price flight found to {destination['city']}!")

        notification_manager.send_emails(email_list=customers_email_list, email_body=message)