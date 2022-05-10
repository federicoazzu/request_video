import requests as rq
from collections import namedtuple

#  URL
base_url = 'https://api.themotivate365.com/stoic-quote'

#  Data Model
Quote = namedtuple('Quote', 'data author quote')


def get_quote() -> Quote:
    # payload = {'query': 'value'}
    request = rq.get(base_url)  # params=payload
    json = request.json()

    data = json['data']
    author = data['author']
    quote = data['quote']

    return Quote(data, author, quote)


# Make the request
result: Quote = get_quote()

print('Author:', result.author)
print('Quote:', result.quote)
