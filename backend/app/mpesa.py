import os
import time
import math
import base64
import requests
from datetime import datetime
from requests.auth import HTTPBasicAuth
from dotenv import load_dotenv

load_dotenv()

class LipaNaMpesa:
    def __init__(self) -> None:
        self.now = datetime.now()
        self.shortcode = os.getenv("SHORTCODE")
        self.consumer_key = os.getenv("CONSUMER_KEY")
        self.consumer_secret = os.getenv("CONSUMER_SECRET")
        self.passkey = os.getenv("PASS_KEY")
        self.access_token_url = os.getenv("ACCESS_TOKEN_API")
        self.stk_push_url = os.getenv("STK_PUSH_API")
        self.access_token = None
        self.call_back = os.getenv("CALLBACK_URL")
        self.access_token_expiration = 0

        try:
            self.access_token = self.get_mpesa_access_token()
            if self.access_token is None:
                raise Exception("Request for access token failed")
            else:
                self.access_token_expiration = time.time() + 3599
        except Exception as e:
            print(str(e))
    
    def get_mpesa_access_token(self):
        try:
            res = requests.get(
                self.access_token_url,
                auth=HTTPBasicAuth(self.consumer_key, self.consumer_secret)
            )
            token = res.json()['access_token']
            self.headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"
            }
        except Exception as e:
            print(str(e), "error getting access token")
            raise e
        return token
    
    def generate_password(self):
        timestamp = self.now.strftime("%Y%m%d%H%M%S")
        password_str = self.shortcode + self.passkey + timestamp
        password_bytes = password_str.encode()
        return base64.b64encode(password_bytes).decode("utf-8")
    
    def stk_push(self, payload):
        amount = payload['amount']
        phone_number = payload['phone_number']
        enrollment_id = payload['enrollment_id']
        password = self.generate_password()
        timestamp = self.now.strftime("%Y%m%d%H%M%S")

        callback_url = f"{self.call_back}/{enrollment_id}"  

        data = {
            "BusinessShortCode": self.shortcode,
            "Password": password,
            "Timestamp": timestamp,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": math.ceil(float(amount)),
            "PartyA": phone_number,
            "PartyB": self.shortcode,
            "PhoneNumber": phone_number,
            "CallBackURL": callback_url,
            "AccountReference": "Pay Enrollment fee",
            "TransactionDesc": "description of the transaction",
        }

        response = requests.post(
            self.stk_push_url,
            json=data,
            headers=self.headers
        )
        return response.json()
