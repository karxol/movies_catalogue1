
from ctypes import cast
import requests 
import os

API_TOKEN = os.environ.get("TMDB_API_TOKEN", "")
#API_TOKEN = "?api_key=0747dfbc9a2d7974a8bba5cd07145c24"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular?api_key=0747dfbc9a2d7974a8bba5cd07145c24"
   
    response = requests.get(endpoint)
    return response.json()

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_movies(how_many=20, list_type="popular"):
    all_movies = get_popular_movies()["results"][:how_many]
    return all_movies


def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    api_token = API_TOKEN
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()


def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits?api_key=0747dfbc9a2d7974a8bba5cd07145c24"
    response = requests.get(endpoint)
    return response.json()["cast"]



def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()







