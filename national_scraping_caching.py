from bs4 import BeautifulSoup # need beautifulsoup for scraping
import requests, json # need these to access data on the internet and deal with structured data in my cache
from advanced_expiry_caching import Cache # use tool from the other file for caching
import csv


states_abbr= ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga', 'hi',
          'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn',
          'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh',
          'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']


for i in range(len(states_abbr)):
    url = "https://www.nps.gov/state/%s/index.htm" % states_abbr[i]
    FILENAME = "%s_national.json" %states_abbr[i]# saved in variable with convention of all-caps constant
    program_cache = Cache(FILENAME) # create a cache -- stored in a file of this name
    data = program_cache.get(url)

    if not data:
        data = requests.get(url).text # get the text attribute from the Response that requests.get returns -- and save it in a variable. This should be a bunch of html and stuff
        program_cache.set(url, data, expire_in_days=1) # just 1 day here because news site / for an example in class
