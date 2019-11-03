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
# Link →<https://api.github.com/repositories/1362490/contributors?page=2>; rel="next", <https://api.github.com/repositories/1362490/contributors?page=14>; rel="last"

# # Set to 1 or true to include anonymous contributors in results.
# response = requests.get(repo_url+'/contributors?anon=1',
#                         headers=request_headers)
# #Link →<https://api.github.com/repositories/1362490/contributors?anon=1&page=2>; rel="next", <https://api.github.com/repositories/1362490/contributors?anon=1&page=22>; rel="last"

print(response.json())
# print(response.headers)
