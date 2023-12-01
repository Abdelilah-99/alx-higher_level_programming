#!/usr/bin/python3
"""
sends a request to the URL and
displays the value of the variable
X-Request-Id in the response header
"""
import requests
import sys

url = sys.argv[1]
response = requests.get(url)
id = response.headers.get('X-Request-Id')
print(id)
