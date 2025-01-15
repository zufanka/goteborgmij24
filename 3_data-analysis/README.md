# Data analysis

In this part we will do some data analysis on the data we have scraped - or any other data for that matter. For that you will need to install the [`jupyter lab`](https://jupyter.org/install) environment, [matplotlib](https://matplotlib.org/stable/) and the [`pandas` library](https://pandas.pydata.org/docs/getting_started/install.html) (please refer to *Installing from PyPI* with `pip`).

## Self-study
To know what to expect, watch this [introduction to pandas video](https://www.youtube.com/watch?v=dcqPhpY7tWk) (10 min)

## Day 1
Introduction to pandas. See the [cheatsheet](https://github.com/zufanka/goteborgmij24/blob/main/3_data-analysis/pandas_cheatsheet.md). We'll be working with 2 datasets (see the folder `data`)

#### Titanic
[data source](https://www.kaggle.com/datasets/vinicius150987/titanic3/data)
[data dictionary](https://choens.github.io/titanic/workshops/regression/data-dictionary/)
#### Cocktails
- [source](https://github.com/rfordatascience/tidytuesday/blob/main/data/2020/2020-05-26/readme.md)
- [tidy tuesday analysis](https://www.youtube.com/watch?v=EC0SVkFB2OU&list=PL19ev-r1GBwkuyiwnxoHTRC8TTqP8OEi8&index=36))

### Homework: reading
1. [Uncovering big tech's hidden network](https://www.somo.nl/uncovering-big-techs-hidden-network/)
2. [Lobbying Bonanza as Firms Try to Influence European Union](https://github.com/zufanka/goteborgmij24/blob/main/3_data-analysis/docs/Lobbying%20Bonanza%20as%20Firms%20Try%20to%20Influence%20European%20Union%20-%20The%20New%20York%20Times.pdf)

## Day 2
With having some idea about what we can do with pandas, we'll dive into a little investigation. See the `data` folder for the files `law_firms-clean.csv` and `clients-clean.csv`.

## Investigation
### Preparation
- Split into groups of 4-5 people
- *20 min* talk about the reading you did and what are possible stories in the data you have
- read about the [angles journalists use most often to tell the stories in data](https://github.com/zufanka/goteborgmij24/blob/main/3_data-analysis/docs/Here%20are%20the%20angles%20journalists%20use%20most%20often%20to%20tell%20the%20stories%20in%20data%20_%20Online%20Journalism%20Blog.pdf)
- *30 min* look through the dataset, look at the columns you have, sort them from largest to lowest, explore the unique values, counts. See what you are missing to make the story you would like to make.
- read [Building a hypothesis for your next data story](https://github.com/zufanka/goteborgmij24/blob/main/3_data-analysis/docs/Building%20a%20hypothesis%20for%20your%20next%20data%20story%20_%20DataJournalism.com.pdf)
- Go into the `template` notebook and fill in the first cell

### Work on the story
- test the hypotheses you formulated
- make a short story from the data (~400 words)

## Tips
- you have 3 hours to do this, don't overthink it. Getting 1 or 2 insights from the data and writing something around that is completely ok
- you can use Ada as your data broker and python whisperer 🐍

## Day 3 - data viz
See the `dataviz` notebook for how to use `matplotlib` and the `altair` libraries.

### Impressive links
- [Altair example gallery](https://altair-viz.github.io/gallery/index.html#example-gallery)
- [Scroll story with Flourish](https://pointer.kro-ncrv.nl/zeldzame-vogels-in-gevaar-door-stikstofvervuiling) - my story on birds being threathened by nitrogen pollution (in Dutch)
- [RAW graphs: the exotic data visualisations](https://app.rawgraphs.io/)
- [The pudding](https://pudding.cool/) - visual data essays
- [Datawrapper blog](https://blog.datawrapper.de/category/datavis-dos-and-donts/) - tips and tricks on choices you make when making a datavisualisation
- []