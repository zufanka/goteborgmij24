## Week 2 & 3
[slides](https://homolova.sk/goteborgmij24/scraping)

[recording](https://youtu.be/RZXZhCrE8pI)


This week we will be scraping the web. For that you will need to install two libraries: [`requests`](https://requests.readthedocs.io/en/latest/) , [`Beautiful Soup`](https://beautiful-soup-4.readthedocs.io/en/latest/), and [`csv`](https://docs.python.org/3/library/csv.html). Optionally install [`jupyter-lab`](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) (version of jupyter notebooks).

Use [`pip`](https://pypi.org/project/pip/) to install libraries. It might be called `pip3` on your system.

This directory also contains `skeleton.py` file with a dummy simple scraper structure. While some of the pages you might want to scrape will follow this structure losely,  please note however that every page is different and requires a bit different approach.

### Self-study

#### preparation
- learn how to use the browser [Developer tools](https://www.youtube.com/watch?v=RBinFeVZz0E). Every browser has these, if you right click on any website you migh see "Inspect element" or "Inspect"
- if you are unfamiliar with HTML, please also watch [this 7 min video on how a website is structured](https://www.youtube.com/watch?v=ipkjfvl40s0)

#### scraping
- rewatch the [scraping video from the class](https://youtu.be/RZXZhCrE8pI?si=g8okdMKBHBBGKrEL&t=1203) and follow along. You can do it 💪 Ask the robots or your classmates for help if you don't understand why I did something.
- *(optional)* watch and follow this [scraping video](https://youtu.be/XVv6mJpFOb0?si=Q8o8EjvfC-drToIR) - this includes instructions on how to install libraries (until 48:20).
- *(optional)* watch and follow [another scraping video](https://www.youtube.com/watch?v=gRLHr664tXA)
- 
#### csv writer
- introduction to the [csv library](https://www.youtube.com/watch?v=q5uM4VKywbA)
- using [csv writer](https://www.youtube.com/watch?v=jnkPnNaLY3g)
- 
### Concepts
You should know how to use these concepts and for what purpose:

#### Python syntax:
- `for` loops
- `if elif else` statements
- `try except` error handling
- `.strip()` - many pages contain loads of trailing whitespaces in improbable places

#### requests:
- `requests.get()`
- `.text`
#### BeautifulSoup
- `beautifulSoup()`
- `soup.find(string="")`
- `soup.select_one()`
- `soup.select()`
- `.text`
- `.get()` - to get attributes out of the tags
- [CSS selectors](https://beautiful-soup-4.readthedocs.io/en/latest/#css-selectors) (to use with `soup.select()`)

#### csv
- `csv.reader()` or `csv.DictReader()`
- `csv.writer()` or `csv.DictWriter()`



### Homework: scrape a website
- chose one or more scrapers from the list below
- 
#### Scraper1 - less code
- watch video on how to look for [API's under websites](https://www.youtube.com/watch?v=6gtHzj4GMLo)
- Scrape the lobbyists data from [integritywatch](https://integritywatch.eu/organizations.php)
- write a script that outputs a csv file with the data
#### Scraper2 - more code
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


[Upload the homework](https://forms.gle/zZhoMTMVrsJ8qzFL8) as a `.py` script by **31.12.2024**

Fill in [short survey](https://forms.gle/CT87GySvCS89UryDA)
