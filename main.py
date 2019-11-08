from utils.getters import fetch
from utils.getters import fetchPagination

from utils.setters import save

# # Detailed representations
# response = fetch()

# # List all topics for a repository, github #topics
# topics = fetch('/topics', {
#     'Accept': 'application/vnd.github.mercy-preview+json'
# })
# save(topics.json(), 'topics.json')

# # List contributors, exclude anonymous contributors
# contributors = fetchPagination('/contributors')
# save(contributors, 'contributors.json')

# # List contributors, including anonymous contributors in results.
# anon_contributors = fetchPagination('/contributors?anon=true')
# save(anon_contributors, 'anon_contributors.json')

# # List languages, counted by Bytes
# languages = fetch('/languages')
# save(languages.json(), 'languages.json')

# # List tags, git tags
# tags = fetchPagination('/tags')
# save(tags, 'tags.json')

# # List branches, excluding protected branches
# branches = fetch('/branches')
# save(branches.json(), 'branches.json')

# # List branches, including protected branches
# protected_branches = fetch('/branches?protected=true')
# save(protected_branches.json(), 'protected_branches.json')

# # List commit comments for a repository, ordered by ascending ID
# comments = fetchPagination('/comments')
# save(comments, 'comments.json')

# # List commit comments for a repository with reactions summary, ordered by ascending ID
# reaction_comments = fetchPagination('/comments', {
#     'Accept': 'application/vnd.github.squirrel-girl-preview',
# })
# save(reaction_comments, 'reaction_comments.json')

# # List commits on a repository, from new to old
# commits = fetchPagination('/commits')
# save(commits, 'commits.json')

# # Retrieve community profile metrics
# community = fetch('/community/profile', {
#     'Accept': 'application/vnd.github.black-panther-preview+json'
# })
# save(community.json(), 'community.json')

# # List all issues for a repository
# issues = fetchPagination('/issues?state=all')
# save(issues, 'issues.json')

# List all pull requests
pulls = fetchPagination('/pulls')
save(pulls, 'pulls.json')
