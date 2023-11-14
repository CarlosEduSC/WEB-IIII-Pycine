import requests

api_key = "fefad9b3c220f91744bb9afb42b64a0e"

genres = [{'id': 28, 'name': 'Action'}, {'id': 12, 'name': 'Adventure'}, {'id': 16, 'name': 'Animation'}, {'id': 35, 'name': 'Comedy'}, {'id': 80, 'name': 'Crime'}, {'id': 99, 'name': 'Documentary'}, {'id': 18, 'name': 'Drama'}, {'id': 10751, 'name': 'Family'}, {'id': 14, 'name': 'Fantasy'}, {'id': 36, 'name': 'History'}, {'id': 27, 'name': 'Horror'}, {'id': 10402, 'name': 'Music'}, {'id': 9648, 'name': 'Mystery'}, {'id': 10749, 'name': 'Romance'}, {'id': 878, 'name': 'Science Fiction'}, {'id': 10770, 'name': 'TV Movie'}, {'id': 53, 'name': 'Thriller'}, {'id': 10752, 'name': 'War'}, {'id': 37, 'name': 'Western'}]

def get_json(endpoint, params=None):

    url = f"https://api.themoviedb.org/3/{endpoint}?api_key={api_key}{params}"

    response = requests.get(url)
    
    return response.json()

def mais_populares():

    data = get_json("discover/movie", "&sort_by=vote_count.desc")

    results = data['results']
    print("="*20)
    for movie in results:
        print(movie['original_title']) 
        print(movie['id']) 
        print(movie['genre_ids'])
        print(movie['vote_count']) 
        print("----")

    print(f"Total: {len(results)}")

# def get_generos():
#     data = get_json("https://api.themoviedb.org/3/genre/movie/list","&language=en")

#     results = data['genres']

#     print(results)

def get_genero_id(id):
    for genre in genres:
        if id == genre["id"]:
            return genre["name"]
    
    return None

def get_movie_by_tittle(tittle):

    data = get_json("search/movie", f"&query={tittle}")

    results = data["results"]

    print(results)

def get_artist_by_name(name):
    data = get_json("search/person", f"&query={name}")

    results = data["results"]

    print(results)

def get_recomendados_semana():
    data = get_json("movie/week", "&language=en-US")

    results = data["results"]

    print(results[:5])


if __name__ == "__main__":
    # mais_populares()
    # get_generos()
    # get_genero_id(28)
    # get_movie_by_tittle("Run")
    # get_artist_by_name("arnold")
    get_recomendados_semana()