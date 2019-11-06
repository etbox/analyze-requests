import requests

token = '455267bfe73cfa83b878b9336820df4f18e59b5b'


def fetch(path=''):
    repo_url = 'https://api.github.com/repos/psf/requests'+path
    request_headers = {
        'Accept': 'application/vnd.github.v3+json',
        'Authorization': 'token {}'.format(token)
    }

    response = requests.get(repo_url, headers=request_headers)
    return response
