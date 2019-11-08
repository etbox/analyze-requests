import requests
import re
import json


def fetch(path='', request_headers={
    'Accept': 'application/vnd.github.v3+json',
}):
    found_full_url = re.findall(r'api.github.com', path)
    url = 'https://api.github.com/repos/psf/requests' + \
        path if len(found_full_url) == 0 else path
    request_headers['Authorization'] = 'token 455267bfe73cfa83b878b9336820df4f18e59b5b'

    response = requests.get(url, headers=request_headers)
    return response


def fetchPagination(path, request_headers):
    first_response = fetch(path, request_headers)
    result_json = first_response.json()
    first_link = first_response.headers['link']
    pagination_info = re.findall(r'<(https://.+?)>;\srel="(\w+)"', first_link)

    # last_page_info = [item for item in pagination_info if item[1] == 'last']
    next_page_info = [item for item in pagination_info if item[1] == 'next']

    while len(next_page_info) != 0:
        # To check whether is fetching
        print(next_page_info[0][0])
        response = fetch(next_page_info[0][0], request_headers)
        result_json = result_json + response.json()
        pagination_info = re.findall(
            r'<(https://.+?)>;\srel="(\w+)"', response.headers['link'])
        next_page_info = [
            item for item in pagination_info if item[1] == 'next']

    return result_json
