import requests
from bs4 import BeautifulSoup as bs
import csv

# this is your startpage
www = ''

# use this to open and read a page
r = requests.get(www)
soup = bs(r.text)


# for example if you want to open multiple links on a page and save something from those
with open("outputfile.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    # this will write a header row
    writer.writerow(["sometext"])
    
    # this selects all the links on the page with class 'imhere'
    for a in soup.select(".imhere a"):
        
        href = a.get("href")
        
        r = requests.get(href)
        soup = bs(r.text)
        
        # select some piece of text in a div element with class 'getme'
        sometext = soup.select(".getme").text
        
        writer.writerow([sometext])
        
    
    

