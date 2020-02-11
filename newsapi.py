
import requests
import secrets

NEWSAPI_KEY = secrets.NEWSAPI_KEY
base_url = 'https://newsapi.org/v2/everything'
params = {
    'q' : 'new hampshire',
    'apiKey' : NEWSAPI_KEY
}

num_results = -1


response = requests.get(base_url, params)
result = response.json()

if (num_results.isnumeric() != 1
    or num_results == -1
    or num_results > len(result['articles'])):
    num_results = len(result['articles'])
for i in range(num_results):
    number = '(' + str(i+1) + ') '
    headline = result['articles'][i]['title']
    source = result['articles'][i]['source']['name']
    line = number + headline + ' [' + source + ']'
    print(line)
    continue