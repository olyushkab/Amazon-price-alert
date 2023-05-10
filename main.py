import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

CONTROLLER_URL = "https://www.amazon.com/Xbox-Elite-Wireless-Controller-Core-Controllers/dp/B0B789CGGQ/ref" \
                 "=sr_1_1_sspa?crid=66JC6YSS47MR&keywords=xbox%2Bcontroller&qid=1679328357&sprefix=xbox%2Bcontroller" \
                 "%2Caps%2C148&sr=8-1-spons&spLa" \
                 "=ZW5jcnlwdGVkUXVhbGlmaWVyPUExNThPTFZXUVNNSENVJmVuY3J5cHRlZElkPUEwODM5ODgyREVUUzhQMEE5TUtXJmVuY3J5cHRlZEFkSWQ9QTAxODk2NjhCVE1WUDRSMFlNRFMmd2lkZ2V0TmFtZT1zcF9hdGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl&th=1 "
HEADER = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/111.0.0.0 Safari/537.36 "
}
MY_EMAIL = "email"
MY_PASSWORD = "password"
RECEIVER_EMAIL = "receiver_email"

# Below price target product becomes unprofitable and needs to be suppressed from website
TARGET_PRICE = 120

response = requests.get(CONTROLLER_URL, headers=HEADER).text

soup = BeautifulSoup(response, "lxml")
price = soup.find(name="span", class_="a-offscreen").getText()
price_without_currency = float(price.split("$")[1])

product_title = soup.find(id="productTitle").get_text().strip()

# SEND EMAIL ALERT
if price_without_currency < TARGET_PRICE:
    message = f"Subject:Price alert for {product_title}\n\n{product_title} is now {price}"

    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=RECEIVER_EMAIL, msg=message)





#used http request to get the product price
#used smtp to send email alert when price goes below profitability threshold