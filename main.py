from utils.getters import fetch
from utils.getters import fetchTopics
from utils.getters import fetchPagination

from utils.setters import save

# # Detailed representations
# response = fetch()

# # List all topics for a repository, github #topics
# topics = fetchTopics()
# save(topics.json(), 'topics.json')

# # List contributors, exclude anonymous contributors
# contributors = fetchPagination('/contributors')
# save(contributors, 'contributors.json')

# # List contributors, including anonymous contributors in results.
# anon_contributors = fetchPagination('/contributors?anon=true')
# save(anon_contributors, 'anon_contributors.json')

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

# print(len(response))
# print(response.headers['link'])
