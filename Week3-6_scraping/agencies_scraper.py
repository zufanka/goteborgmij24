#!/usr/bin/env python
# coding: utf-8

import requests
import csv
# bs is an alias for BeautifulSoup
from bs4 import BeautifulSoup as bs


with open('agencies.csv', 'w') as csvfile:
    # create a writer for our file
    csvwriter = csv.writer(csvfile, delimiter=',')
    # this is our header
    csvwriter.writerow(["abbreviation", "type", "agency", "commissioner"])

    # there are three pages we need to go through
    for n in range(3):
        
        # f strings allow us to combine strings and variables
        url = f"https://commission.europa.eu/about/departments-and-executive-agencies_en?page={n}"
    
        # get the website as plaintext
        r = requests.get(url)
    
        # make the plaintext into something BeautifulSoup can work with
        soup = bs(r.text)

        links = soup.select(".ecl-card__body a")
    
        for a in links:
            # get the href attribute out of the element
            href = a.get("href")
            
            if href.startswith('https://'):
                continue
            
            print(href)
    
            r = requests.get(f"https://commission.europa.eu{href}")
            soup = bs(r.text)

            # find the string "Commissioner" in the page
            findcommissioner = soup.find(string="Commissioner")

            # handle cases where abbreviation is not on the page
            try:
                abbreviation = soup.select(".ecl-page-header__info li")[1].text
            except IndexError:
                abbreviation = ""
            
            type = soup.select(".ecl-page-header__info li")[0].text
            agency = soup.select_one(".ecl-page-header__info h1").text

            # sometimes there is no commissioner, let's handle that
            if findcommissioner != None:
                commissioner = findcommissioner.parent.parent.a.text
                csvwriter.writerow([abbreviation, type, agency, commissioner])
            
            else:
                csvwriter.writerow([abbreviation, type, agency, ""])





