<img src="https://github.com/ZanClifton/intermediate-python-projects/blob/main/images/pollen-scraper.png" width=250px align=right alt="Pollen Scraper"/>

# Pollen Scraper

I have terrible hayfever, so I like to know what I'm going to be facing every day. I'm also really bad at remembering to check what the pollen count is.

This is a Python project which uses BeautifulSoup to scrape the pollen breakdown from [The Weather Channel site](https://weather.com/) and save it in a text file.

The pollen data is the only information which is saved in the `<strong>` tags on the requisite page, and BeautifulSoup creates a list of the tags in sequence. Utilising the array position for the string in each tag, it's possible to construct a string with a 3 day forecast of the pollen count for tree, grass and ragweed pollen.

These results are output to:

- `data.txt`

To run this locally, you will need to install BeautifulSoup and the Requests module:

```
$ pip install beautifulsoup4
$ pip install requests
```

Instructions for creating a local copy are available in the main [README.md file](https://github.com/ZanClifton/intermediate-python-projects/blob/main/README.md).
