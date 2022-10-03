
import requests

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular?api_key=0747dfbc9a2d7974a8bba5cd07145c24"
   
    response = requests.get(endpoint)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

