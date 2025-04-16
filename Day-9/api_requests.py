import requests
#requests module allows us to talk/connect with the api of the github.
response=requests.get("https://api.github.com/repos/kubernetes/kubernetes/pulls")
details=response.json() #here response.json() internally converts json output to the dictionary 
for i in range(len(details)):
    print(details[i]["user"]["id"]) # ""i" is the index/element  of list which is dictionary(user) and "id" is key for user


