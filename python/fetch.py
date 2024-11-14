import requests

url = "https://api.github.com/repos/nmagee/ds2002-course/branches"

#setting up an object to put the info we're getting from the url into 
response = requests.get(url)

# get out the name objects -> in this case we're listing all the branches 
for r in response.json():
  print(r['name']) 
