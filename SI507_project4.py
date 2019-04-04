from bs4 import BeautifulSoup
import requests
import json
import csv
states_abbr= ['al', 'ak', 'az', 'ar', 'ca', 'co', 'ct', 'dc', 'de', 'fl', 'ga', 'hi',
          'id', 'il', 'in', 'ia', 'ks', 'ky', 'la', 'me', 'md', 'ma', 'mi', 'mn',
          'ms', 'mo', 'mt', 'ne', 'nv', 'nh', 'nj', 'nm', 'ny', 'nc', 'nd', 'oh',
          'ok', 'or', 'pa', 'ri', 'sc', 'sd', 'tn', 'tx', 'ut', 'vt', 'va', 'wa', 'wv', 'wi', 'wy']

with open('national_parks.csv','w') as f:
    national_write = csv.writer(f)
    national_write.writerow(["Type", "Name", "Location", "Description","Challenge State"])
    for i in range(len(states_abbr)):
        with open('%s_national.json'%states_abbr[i]) as json_f:
            national_data = json.load(json_f)
            soup = national_data["HTTPS://WWW.NPS.GOV/STATE/%s/INDEX.HTM"%states_abbr[i].upper()]['values']
            soup = BeautifulSoup(soup, features="html.parser")
            titles = soup.select("div[class='col-md-9 col-sm-9 col-xs-12 table-cell list_left']")
            states = []
            for j in range(len(titles)):
                #Type of the site
                a = titles[j].find('h2').get_text()
                if not a:
                    a = "Default National Park"
                #Name of the site
                b = titles[j].find('h3').get_text()
                if not b:
                    b = "NA"
                #Location of the site
                c = titles[j].find('h4').get_text()
                if not c:
                    c = states_abbr[i].upper()
                #Description of the site
                d = titles[j].find('p').get_text()
                if not d:
                    d = "NA"
                #CHALLENGE State
                challenge_state = []
                for k in range(len(states_abbr)):
                    if states_abbr[k].upper() in c:
                        challenge_state.append(states_abbr[k].upper())
                states.append(challenge_state)
                states[j]=",".join(states[j])


                national_write = csv.writer(f)
                national_write.writerow([a, b, c, d,states[j]])
