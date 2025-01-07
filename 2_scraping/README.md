## Scraping
[slides](https://homolova.sk/goteborgmij24/scraping)

[recording 1](https://youtu.be/RZXZhCrE8pI) - see also the [agencies scraper]()

[recording 2]() - see also the [transparency scraper]()

These weeks we will be scraping the web. For that you will need to install two libraries: [`requests`](https://requests.readthedocs.io/en/latest/) , [`Beautiful Soup`](https://beautiful-soup-4.readthedocs.io/en/latest/), and [`csv`](https://docs.python.org/3/library/csv.html). Optionally install [`jupyter-lab`](https://jupyterlab.readthedocs.io/en/stable/getting_started/installation.html) (version of jupyter notebooks).

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
 
#### csv writer
- introduction to the [csv library](https://www.youtube.com/watch?v=q5uM4VKywbA)
- using [csv writer](https://www.youtube.com/watch?v=jnkPnNaLY3g)
 
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

### Homework 1: scrape a website

#### scraper 1
- Scrape law firms from the current [Transparency register](https://transparency-register.europa.eu/searchregister-or-update/search-register_en)
- Create a csv table that contains 3 columns: `Organisation’s identification number`, `Organisation name` and the `organisation url`
- loop over all the pages to get all the law firms
- you can use the `skeleton.py` as a backbone for this scraper
- tip: pay attention to the URL

Upload the script named v[Upload the homework](https://forms.gle/zZhoMTMVrsJ8qzFL8) as `scraper1_yourname.py` by **15.12.2024**

Send me your [questions about scraping](https://forms.gle/KSewqkdE6Ck3rfWu9) or Python / programming in general to handle during our next session together

#### scraper 2
- use the previous scraper as your starting point
- From each law firm scrape:
	- the table under "Profile of registrant"
	- table under "Persons accredited for access to European Parliament premises"
	- Clients in the most recent closed financial year
- write a script that outputs 3 csv files:
	1. containing all the information about the law firm from the table under "Profile of registrant"
	2. with all the people accredited for access 
	3. their clients.
	 
	Make sure that every table contains the **REG Number** of the organisation so we are to connect them information to one another. See the data [structure in this table](https://docs.google.com/spreadsheets/d/1IqIGa3rSzWroigOp1llXD47qLfVvmvxo-xrMdP5ZQRU/edit?gid=0#gid=0)

Upload the script named v[Upload the homework](https://forms.gle/zZhoMTMVrsJ8qzFL8) as `scraper2_yourname.py` by **05.01.2025**

### Homework 2
You can chose between a super simple scraper and a more complex one:

#### Single page, no pagination
[Countries of the World](https://www.scrapethissite.com/pages/simple/)
- scrape this page and output a csv with the header : `name, capital, population, area`

#### Including pagination and details
[Books to scrape](http://books.toscrape.com/)

- scrape this page and output a csv with the header: `title, price, star_rating, url`
- if you like you can also add the `description` of the book by going into the url of the books

Upload the script named v[Upload the homework](https://forms.gle/sdFnXi87ETkSd2xd6) as `scraper3_yourname.py` by **12.01.2025**

Please fill in [short survey](https://forms.gle/CT87GySvCS89UryDA) on the scraping part