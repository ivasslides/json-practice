import json 

myvals = [{"repo_name":"json-practice", "repo_url":"https://github.com/nmagee/json-practice/"}, {"repo_name":"fastapi-demo", "repo_url":"https://github.com/nmagee/fastapi-demo/"}]

# taking an array and dumping it into json by using the json.dumps command
myjson = json.dumps(myvals)
print(myjson)