# Scraping the CMU directory
CMU doesn't provide an index that you can just scroll through, but it does provide a [search engine](https://directory.andrew.cmu.edu/) that you can use to look up specific people.

More than the solving of a trivial problem, this is more an exploration into the use of BeautfulSoup and Mechanize for crawling through webpages for data

You can store the data by using the following command

```bash
python scrape.py > out.json
```