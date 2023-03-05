# Carousell-Image-Downloader
### Carousell Image Scraper
### Tested on Carousell(MY) I don't know about SG, PH and others. Haven't tested sorry.

This [Python](https://www.python.org/) script is designed to scrape images and metadata from a Carousell listing and save them locally. The script uses ``Scrapy`` and ``BeautifulSoup`` to extract the necessary data from the webpage, and uses ``PySimpleGUI`` for the GUI.

When the user enters a Carousell URL into the GUI and clicks the "Scrape" button, the script initializes a CrawlerProcess object and passes it an instance of the CarousellSpider class, along with the provided URL as a start URL. The CarousellSpider class defines the parsing logic for the spider. It extracts the name of the item being sold and the URLs of any images on the listing that contain the word "progressive" in their filename. It then saves the images and metadata (item name) to a local directory, which is created in the same location as the script.

## !!NOTE!!
The script will save the images and metadata in a new folder created in the same location as the script. The naming convention for the folder will include the user link ID and item name, along with a random 6-character string of uppercase letters and digits to ensure a unique folder name.

## The Script has issues. 
- It downloads not only the item images but also the comment images.
- The script fails to extract the user link ID from the product page, resulting in the output being marked as an "Unknown User". I haven't been able to fix this.
- Apparently it won't save as .jpg. I will fix this hopefully
- Can't download image if same runtime.
    - Additional Fix for now : Press "X" button (Close) or Alt+F4. And open it again to download another link.
    Again, I will hopefully fix this. 
- Send at Issues tab you find any. Thanks

# Using the App

## Windows
```
pip install scrapy
pip install bs4
pip install PySimpleGUI
```

And then, add Scrapy to your PATH:

    Open the start menu and search for "Environment Variables".
    Click on "Edit the system environment variables".
    Click on the "Environment Variables" button.
    Under "System Variables", scroll down to find "Path" and click on "Edit".
    Click on "New" and add the path to the Scrapy executable folder. Example "C:\Users\Administrator\appdata\local\package\pythonsoftwarefoundation.python.3.10_qbz5n2kfra8p0\localcache\local-packages\python310\Scripts".
    Click "OK" on all open windows to save the changes.

And open up IDLE Editor, Run the script by pressing F5

## Linux
???

## MacOS
???
