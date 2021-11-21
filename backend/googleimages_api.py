from google_images_search import GoogleImagesSearch

API_KEY = 'AIzaSyAJOKrRkt44bdPNdwBEFeR8QzgBkTWqmLc'
PROJECT_CX = 'ac62a5a5d4b56d944'

def get_image(query):
    gis = GoogleImagesSearch(API_KEY,  PROJECT_CX)
    _search_params = {
        'q': query,
        'num': 1
    }
    gis.search(search_params=_search_params)
    return gis.results()[0].url