import requests
import random
import uuid
from datetime import datetime

#todo
url = "asdf"


def post_one_order(person_name, show_name, date, num_of_tickets, price):
    payload = {'Person-name': person_name,
               'Show-name': show_name,
               'date': date,
               'Number-of-tickets': num_of_tickets,
               'Price': price}
    r = requests.post(url, data=payload)
    print(r.status_code)


for x in range(10):
    person_name = str(uuid.uuid4())
    show_name = random.choice(["Jumanji", "Rocky"])
    date = datetime.today().strftime('%Y/%m/%d')
    num_of_tickets = random.randint(0, 30)
    price = 30 * num_of_tickets
    # print([person_name, show_name, date, num_of_tickets, price])
    # post_one_order(person_name, show_name, date, num_of_tickets, price)
