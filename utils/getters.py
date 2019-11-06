import requests

token = '455267bfe73cfa83b878b9336820df4f18e59b5b'


def baseFetch(path='', request_headers={
    'Accept': 'application/vnd.github.v3+json',
    'Authorization': 'token {}'.format(token)
}):

    def closure():
        repo_url = 'https://api.github.com/repos/psf/requests'+path

        response = requests.get(repo_url, headers=request_headers)
        return response

    return closure()


def fetch(path=''):
    return baseFetch(path)


def fetchTopics():
    return baseFetch('/topics', {'Accept': 'application/vnd.github.mercy-preview+json'})
