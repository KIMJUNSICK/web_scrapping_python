import requests

indeed_result = requests.get("https://www.indeed.co.uk/jobs?q=python&limit=50")

print(indeed_result)  # Response 200 => success !

print(indeed_result.text)
# get all html ! # we need to pick out data we want to get
