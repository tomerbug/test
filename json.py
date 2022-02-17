import json
import requests


getNum = input('enter a number: ')

site= requests.get(f'https://jsonplaceholder.typicode.com/posts/{req}')


print(site.content)

