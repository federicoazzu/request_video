import requests as rq
from collections import namedtuple

# URL
base_url = 'http://epicuserpython.pythonanywhere.com/api'

Response = namedtuple('Response', 'accuracy input response')


def get_response(user_input) -> Response:
    payload = {'input': user_input}
    request = rq.get(base_url, params=payload)
    json = request.json()

    print(json)

    accuracy = json['accuracy']
    input = json['input']
    response = json['response']

    return Response(accuracy, input, response)


response: Response = get_response(input('Type something: '))

print('Accuracy:', response.accuracy)
print('Input:', response.input)
print('Response:', response.response)