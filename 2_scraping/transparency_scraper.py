#!/usr/bin/env python
# coding: utf-8


import requests
from bs4 import BeautifulSoup as bs
import csv

badurl = "https://transparency-register.europa.eu/searchregister-or-update/search-register_en?from=&to=&lastUpdateFrom=&lastUpdateTo=&status=&categories=category.cabinetsavocats&numberPersonOF.operator=1&numberPersonOF.value=&numberPersonOF.min=&numberPersonOF.max=&numberFTEPersonOF.operator=1&numberFTEPersonOF.value=&numberFTEPersonOF.min=&numberFTEPersonOF.max=&numberEPAccreditedPersonOF.operator=1&numberEPAccreditedPersonOF.value=&numberEPAccreditedPersonOF.min=&numberEPAccreditedPersonOF.max=&annualCostOF.operator=1&annualCostOF.value=&annualCostOF.min=&annualCostOF.max=&annualRevenueOF.operator=1&annualRevenueOF.value=&annualRevenueOF.min=&annualRevenueOF.max=&totalBudgetOF.operator=1&totalBudgetOF.value=&totalBudgetOF.min=&totalBudgetOF.max=&grantsClosedOF.operator=1&grantsClosedOF.value=&grantsClosedOF.min=&grantsClosedOF.max=&grantsCurrentOF.operator=1&grantsCurrentOF.value=&grantsCurrentOF.min=&grantsCurrentOF.max=&action=submit"

with open("law-firms.csv", "w") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["ID", "name", "url"])
    
    for n in range(0,3):
    
        url = f"https://ec.europa.eu/transparencyregister/public/search/advanced?lang=en&from=&to=&lastUpdateFrom=&lastUpdateTo=&status=&categories=category.cabinetsavocats&numberPersonOF.operator=1&numberPersonOF.value=&numberPersonOF.min=&numberPersonOF.max=&numberFTEPersonOF.operator=1&numberFTEPersonOF.value=&numberFTEPersonOF.min=&numberFTEPersonOF.max=&numberEPAccreditedPersonOF.operator=1&numberEPAccreditedPersonOF.value=&numberEPAccreditedPersonOF.min=&numberEPAccreditedPersonOF.max=&annualCostOF.operator=1&annualCostOF.value=&annualCostOF.min=&annualCostOF.max=&annualRevenueOF.operator=1&annualRevenueOF.value=&annualRevenueOF.min=&annualRevenueOF.max=&totalBudgetOF.operator=1&totalBudgetOF.value=&totalBudgetOF.min=&totalBudgetOF.max=&grantsClosedOF.operator=1&grantsClosedOF.value=&grantsClosedOF.min=&grantsClosedOF.max=&grantsCurrentOF.operator=1&grantsCurrentOF.value=&grantsCurrentOF.min=&grantsCurrentOF.max=&action=submit&page={n}"
    
        r = requests.get(url)
        soup = bs(r.text)
    
        for row in soup.select(".ecl-table__row"):
        
            if len(row.select('th')) > 0:
                continue
                
           #     header = []
           #     for th in soup.select(".ecl-table__row")[0].select('th'):
           #         header.append(th.text)
           #     writer.writerow(header)

            row = row.select("td")
        
            name = row[1].text.strip()
            ID = row[0].text.strip()
            link = row[0].a.get('href')
            full_link = f"https://transparency-register.europa.eu/searchregister-or-update/organisation-detail_en{link.replace('search-details_en','')}" 
    
            writer.writerow([ID, name, full_link])

