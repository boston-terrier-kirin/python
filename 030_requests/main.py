import os
import time
from dotenv import load_dotenv

from libs.openexchange import OpenExchangeClient

load_dotenv(verbose=True)

APP_ID = os.environ.get("APP_ID")

client = OpenExchangeClient(APP_ID)
print(client.latest)

usd_amount = 1

start = time.time()
jpy_amount = client.convert(usd_amount, "USD", "JPY")
end = time.time()
print(end - start)

print(jpy_amount)
