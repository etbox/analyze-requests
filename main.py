import requests

# Detailed representations
repo_url = 'https://api.github.com/repos/psf/requests'
request_headers = {'Accept': 'application/vnd.github.v3+json'}
# response = requests.get(repo_url, headers=request_headers)

# # List all topics for a repository
# request_headers = {'Accept': 'application/vnd.github.mercy-preview+json'}
# response = requests.get(repo_url+'/topics', headers=request_headers)

# List contributors
response = requests.get(repo_url+'/contributors', headers=request_headers)

print(response.json())
# print(response.headers)
