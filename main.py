import requests
r = requests.get('https://api.github.com/repos/psf/requests')
print(r.json()["description"])
