import curses
from google_images_search import GoogleImagesSearch

API_KEY = 'AIzaSyA7YhCenjjTQQCNReyzes3S6dCJKv4BbH8'
PROJECT_CX = 'ff0ffdcf81de586e4'

def get_image(query):
    gis = GoogleImagesSearch(API_KEY,  PROJECT_CX)
    _search_params = {
        'q': query,
        'num': 1
    }
    gis.search(search_params=_search_params)
    return gis.results()[0].url
