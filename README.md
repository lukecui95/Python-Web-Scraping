# Scraping & dealing with data - Pengwei Cui

In this project, first I used caching to store all the National Sites data into json files. Then, I extracted the useful data for each sites from the json files and saved the data in a .CSV file such that each row represents 1 national site. Moreover, I reasonably handled all errors.


## Python files
### national_scraping_caching.py

This file is used to cache all the data on the National Parks websites. We created one json file for each state to save all the national parks' data in that state.

### advanced_expiry_caching.py

The previous python file will use this file to cache all the data and save the data into json files.


### SI507_project4.py

We use this file to extract the data we need in each json file and save the data in a .CSV file. 

First, I got the useful data from a json file and then used BeautifulSoup to handle the data in HTML format. 

Then, I saved the type of the site in the first column, the name of the site in the second column, the location of the site in the third column, the description of the site in the fourth column and the challenge states in the fifth column.

Here's how I handle the errors. If the type of the site is none, I'll fill it with "Default National Park". If the name or the description of the site is none, I'll fill the name or the description with "NA". If the location of the site is none, I'll fill it with the State's abbreviation, since I search national parks by states.  As for the challenge states, I'll search all the states written in the loaction of the site, save them in the states variable and write the variable in the last column in my .CSV file.

## How to run my project

1) Use requirements.txt to set your virtual environment

2) cd to the place you saved my files, and then type at the command prompt: python national_scraping_caching.py

This command is used to cache all the json files from the website.

3) Type at the command prompt: python SI507_project4.py 

This command is to extract data from json files, handle all the errors and save the data in a .CSV file.

## Use requirements.txt to set your virtual environment

1) Create a virtual environment

python3 -m venv project4-env

2) Activate your virtual environment

source project4-env/bin/activate    # For Mac/Linux...

source project4-env/Scripts/activate    # For Windows

3) Install all requirements

pip install -r requirements.txt


4) Try our Flash app

See "How to run our Flash app"

5) Deactivate

deactivate

