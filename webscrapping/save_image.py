import requests

r = requests.get('https://requests.readthedocs.io/en/latest/_static/requests-sidebar.png')

with open('image.png', 'wb') as file:
    file.write(r.content)

# es lo mismo que:

# file = open('image.png', 'wb')
# file.write(r.content)
# file.close()

