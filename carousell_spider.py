import os
import requests
import string
import random
import scrapy
from scrapy.crawler import CrawlerProcess
from bs4 import BeautifulSoup
import PySimpleGUI as sg

class CarousellSpider(scrapy.Spider):
    name = 'carousell'
    allowed_domains = ['carousell.com']
    start_urls = []

    def parse(self, response):
        # Extract item name
        item_name_elem = response.css('.D_aJ.D_tt.D_rY.D_ty.D_t_.D_tC::text').get()
        if item_name_elem:
            item_name = f"F{random.randint(1000, 9999)} - {item_name_elem.strip()}"
        else:
            item_name = "Unknown Item"

        # Extract user link id
        user_link_elem = response.css('a._1VjN3._3aj3V._3v_IH._3VZlL._3cMMi._1jX9b._2ybnq')
        if user_link_elem:
            user_link_id = user_link_elem.attrib['href'].split("/")[-1]
        else:
            user_link_id = "Unknown User"

        # Create directory to save images
        dir_name = f"{user_link_id}-{item_name}".replace(" ", "-") + "-" + ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        if not os.path.exists(dir_name):
            os.makedirs(dir_name)

        # Download images with "progressive" in the filename
        images = response.css('img[src*=progressive]')
        for image in images:
            image_url = image.attrib['src']
            response = requests.get(image_url)
            filename = os.path.join(dir_name, image_url.split("/")[-1])
            with open(filename, "wb") as f:
                f.write(response.content)
                print(f"Downloaded {filename}")

        # Save item name and user link id to a text file
        with open(os.path.join(dir_name, "metadata.txt"), "w") as f:
            f.write(f"Item Name: {item_name}\n")
            f.write(f"User Link ID: {user_link_id}\n")

        yield {'item_name': item_name, 'user_link_id': user_link_id}

def run_spider(url):
    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json'
    })

    process.crawl(CarousellSpider, start_urls=[url])
    process.start()

    with open('output.json') as f:
        data = f.read()

    return data

# Define the layout of the GUI
layout = [
    [sg.Text('Enter a Carousell URL to scrape:')],
    [sg.Input(key='-URL-')],
    [sg.Button('Scrape'), sg.Button('Exit')],
    [sg.Output(size=(80, 20))]
]

# Create the GUI window
window = sg.Window('Carousell Scraper', layout)

# Event loop to process GUI events
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break
    elif event == 'Scrape':
        url = values['-URL-']
        print(f"Scraping {url}...")
        data = run_spider(url)
        print(data)

# Close the GUI window
window.close()
