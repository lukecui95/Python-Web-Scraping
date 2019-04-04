from bs4 import BeautifulSoup
import requests
import json
import csv
states_abbr= ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga', 'hi',
          'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn',
          'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh',
          'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']



with open('national_parks.csv','w') as f:
    for i in range(len(states_abbr)):
        with open('%s_national.json'%states_abbr[i]) as json_f:
            national_data = json.load(json_f)
            soup = national_data["HTTPS://WWW.NPS.GOV/STATE/%s/INDEX.HTM"%states_abbr[i].upper()]['values']
            soup = BeautifulSoup(soup, features="html.parser")
            titles = soup.select("div[class='col-md-9 col-sm-9 col-xs-12 table-cell list_left']")

            for j in range(len(titles)):
                a = titles[j].find('h2')
                if not a:
                    a = "Default National Park"
                b = titles[j].find('h3')
                if not b:
                    b = "NA"
                c = titles[j].find('h4')
                if not c:
                    c = states_abbr[i].upper()
                d = titles[j].find('p')
                if not d:
                    d = "NA"

                national_write = csv.writer(f)
                national_write.writerow([a.get_text(), b.get_text(), c.get_text(), d.get_text(),states_abbr[i].upper()])
