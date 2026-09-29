import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class DataManager:

    def __init__(self):
        self._endpoint = os.environ["SHEETY_PRICES_ENDPOINT"]
        self._customer_endpoint = os.environ["CUSTOMER_RESPONSE_ENDPOINT"]
        self._token = os.environ["SHEETY_TOKEN"]
        self.destination_data = {}
        self.customers_data = {}

    def get_destination_data(self):
        # 2. Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=self._endpoint, headers = {"Authorization": f"Bearer {self._token}"})
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "price": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{self._endpoint}/{row_id}",
            json=new_data,
            headers = {"Authorization": f"Bearer {self._token}"}
        )

    def get_customers_emails(self):
        response = requests.get(url = self._customer_endpoint, headers = {"Authorization": f"Bearer {self._token}"} )
        data = response.json()
        self.customers_data = data["users"]
        return self.customers_data
