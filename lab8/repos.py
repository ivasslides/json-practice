#!/bin/env python3 

import json

# read file in as json, limiting to first 5 lines
with open("../data/schacon.repos.json", "r") as file: 
     data = json.load(file)[:5] 


# creating csv file and appending the 4 fields to each line 
with open("chacon.csv", "w") as csv_file: 
     for item in data:
         line = f"{item.get('name', '')},{item.get('html_url', '')},{item.get('updated_at', '')},{item.get('visibility', '')}\n"
         csv_file.write(line)


