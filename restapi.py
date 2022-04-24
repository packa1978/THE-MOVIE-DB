import requests
import pandas as pd
from Key import api_key

#  make sure that you have downloaded requests from python packages
#  what is our endpoint ( or our url)-  where is it that we want to request data from

# print(r.status_code)
# print(r.text)

# searching for a specific movie based on its title
api_version = 3
api_base_url = f"https://api.themoviedb.org/{api_version}"  # base to the API
endpoint_path = f"/search/movie"  # resource path
search_query = 'Avengers'
endpoint = f"{api_base_url}{endpoint_path}?api_key={api_key}&query={search_query}"  # is it where we request data from
# print(endpoint)
r = requests.get(endpoint)  # call request
print(r.json())

output = 'movies.csv'
movie_data = []
if r.status_code in range(200, 299):
    data = r.json()
    # print(type(data)) # response is a dictionary
    results = data['results']
    if len(results) > 0:
        # print(results[0].keys()) # quick view of the keys available
        movie_ids = set()
    for result in results:
        _id = result['id']
        print(result['title'], _id)  # to print out the list different titles that are related by title with id
        movie_ids.add(-_id)
        # print(list(movie_ids))

        for movie_id in movie_ids:
            data_id = r.json()
            movie_data.append(data_id)

#print(movie_data)

df = pd.DataFrame(movie_data)
print(df.head())
df.to_csv(output, index=True)
