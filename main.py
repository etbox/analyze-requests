from utils.getters import fetch
from utils.getters import fetchTopics

from utils.setters import save

# # Detailed representations
# response = fetch()

# # List all topics for a repository, github #topics
# response = fetchTopics()
# save(response.json(), 'topics.json')

# List contributors
response = fetch('/contributors')
# Link →<https://api.github.com/repositories/1362490/contributors?page=2>; rel="next", <https://api.github.com/repositories/1362490/contributors?page=14>; rel="last"

# # List contributors, including anonymous contributors in results.
# response = requests.get(repo_url+'/contributors?anon=1',
#                         headers=request_headers)
# #Link →<https://api.github.com/repositories/1362490/contributors?anon=1&page=2>; rel="next", <https://api.github.com/repositories/1362490/contributors?anon=1&page=22>; rel="last"

# # List languages, counted by Bytes
# response = requests.get(repo_url+'/languages', headers=request_headers)

# # List tags, git tags
# response = requests.get(repo_url+'/tags', headers=request_headers)
# # Link →<https://api.github.com/repositories/1362490/tags?page=2>; rel="next", <https://api.github.com/repositories/1362490/tags?page=5>; rel="last"

# # List branches, including protected branches
# response = requests.get(repo_url+'/branches', headers=request_headers)

# List commit comments for a repository, ordered by ascending ID
# response = requests.get(repo_url+'/comments', headers=request_headers)
# Link →<https://api.github.com/repositories/1362490/comments?page=2>; rel="next", <https://api.github.com/repositories/1362490/comments?page=12>; rel="last"

print(response.json())
# print(response.headers)
