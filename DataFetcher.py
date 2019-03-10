import requests
import json
import tempfile
import urllib.request


def fetchMovieContent(query):
    apiURL = 'https://www.omdbapi.com/?apikey=6535efc2&t={}&type=movie'.format(query)
    try:
        response = requests.get(apiURL)
        jsonData = json.loads(response.text)
        imageUrl = jsonData['Poster']
        resource = urllib.request.urlopen(imageUrl)
        imageFile = open(query + ".jpg", "wb")
        imageFile.write(resource.read())
        imageFile.close()
        return (jsonData, imageFile.name)
    except Exception as error:
        print(error)

