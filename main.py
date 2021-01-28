import requests

response = requests.post(
    'https://api.remove.bg/v1.0/removebg',
    files={'image_file': open('IMAGE LOCATION HERE', 'rb')},
    data={'size': 'auto'},
    headers={'X-Api-Key': 'j2D5GtLi4Grdj8QJLSxq8cBc'},
)
try:
    f = open('removed.png', 'wb')
    f.write(response.content)
except Exception as e:
    print("Error", e)
