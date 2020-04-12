#!/usr/bin/env python3
# if error, register with python console
# yagmail.register(user, pass)
import yagmail

import requests
from bs4 import BeautifulSoup

# get webpage with COVID19 statistics
URL = 'https://www.worldometers.info/coronavirus/'
page = requests.get(URL)

# parse the page through BS
soup = BeautifulSoup(page.content, 'html.parser')

# find our maincounter elements. we'll get our numbers
# from the span element within
results = soup.find_all(class_='maincounter-number')

# send the email to my mobile number
receiver = 'put a receiving email here'

# build the body of the email with a multi line string
body = f"So far {results[0].span.text} people have been infected with COVID19. {results[1].span.text} have died from the disease. However, {results[2].span.text} have also recovered."

# send the email using yag
yag = yagmail.SMTP('put your own email here').send(
    to=receiver,
    subject='COVID19',
    contents=body
)