## Week 2 & 3
[slides](https://homolova.sk/goteborgmij24/scraping)


This week we will be scraping the web. For that you will need to install two libraries: [`requests`](https://requests.readthedocs.io/en/latest/) , [`Beautiful Soup`](https://beautiful-soup-4.readthedocs.io/en/latest/), and [csv](https://docs.python.org/3/library/csv.html)
### Self-study
#### scraping
- rewatch the scraping video from the class
- watch and follow this [scraping video](https://youtu.be/XVv6mJpFOb0?si=Q8o8EjvfC-drToIR) - this includes instructions on how to install libraries (until 48:20)
- (optional) watch and follow [another scraping video](https://www.youtube.com/watch?v=gRLHr664tXA)
#### csv writer
- introduction to the [csv library](https://www.youtube.com/watch?v=q5uM4VKywbA)
- using [csv writer](https://www.youtube.com/watch?v=jnkPnNaLY3g)
### Concepts
These are functions from the two libraries you should know how to use and for what purpose:
- `requests.get()`
- `beautifulSoup()`
- `soup.find_all()`
- `soup.select() & CSS selectors`
- `csv.reader()` or `csv.DictReader()`
- `csv.writer()` or `csv.DictWriter()`

### Homework: scrape a website
- chose one or more scrapers from the list below
#### Easy scraper
- watch video on how to look for [API's under websites](https://www.youtube.com/watch?v=6gtHzj4GMLo)
- Scrape the lobbyists data from [integritywatch](https://integritywatch.eu/organizations.php)
- write a script that outputs a csv file with the data
#### Simple scraper
- Scrape law firms from the current [Transparency register](https://transparency-register.europa.eu/searchregister-or-update/search-register_en)
- From each law firm scrape:
	- the table under "Profile of registrant"
	- table under "Persons accredited for access to European Parliament premises"
	- Clients in the most recent closed financial year
- write a script that outputs 3 csv files:
	1. containing all the information about the law firm from the table under "Profile of registrant"
	2. with all the people accredited for access 
	3. their clients.
	 
	Make sure that every table contains the **REG Number** of the organisation so we are to connect them information to one another. See the data [structure in this table](https://docs.google.com/spreadsheets/d/1IqIGa3rSzWroigOp1llXD47qLfVvmvxo-xrMdP5ZQRU/edit?gid=0#gid=0)
#### Complex scraper
(contact me if you chose this one)
- watch the network tab deep dive [video](https://www.youtube.com/watch?v=DqtlR0y0suo)
- scrape the Law firms from the [lobbyfacts website](https://www.lobbyfacts.eu/)
	- learn about `requests.post()`
	- tip: use the network tab and `copy as curl` + [curlconverter](https://curlconverter.com/)
- write a script that outputs 3 csv files:
	1. containing all the information about the law firm from the table under "Overview" per year
	2. with all the people accreddited for access with a start and end date
	3. their clients per year

[Upload the homework](https://forms.gle/zZhoMTMVrsJ8qzFL8) as a `.py` script 

Fill in [short survey](https://forms.gle/CT87GySvCS89UryDA)