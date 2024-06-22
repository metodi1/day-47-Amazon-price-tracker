import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "html.parser")

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)




title = soup.find(id="productTitle").get_text().strip()

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        result = connection.login('metodiganev207@gmail.com', 'cdig caxq axff idok')
        connection.sendmail(
            from_addr="metodiganev207@gmail.com",
            to_addrs="metodiganev207@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{message}\n{url}".encode("utf-8")
        )