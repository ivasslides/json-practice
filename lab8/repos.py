#!/bin/env python3 

import json

fields = ["name", "html_url", "updated_at", "visibility"]

# read file in as json 
with open("../data/schacon.repos.json", "r") as file: 
     data = json.load(file)[:5] 


# creating csv file and appending 4 fields to each line 
with open("chacon.csv", "w") as csv_file: 
     # limiting to 5 lines
     for item in data:
         #line = [str(item.get(field, "")) for field in fields]
         #csv_file.write(",".join(line) + "\n")
         line = f"{item.get('name', '')},{item.get('html_url', '')},{item.get('updated_at', '')},{item.get('visibility', '')}\n"
         csv_file.write(line)


