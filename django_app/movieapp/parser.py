import json
import urllib.request
from movieapp.models import MovieInfo

url = "https://yts.am/api/v2/list_movies.json?"
page_param = 1
limit_param = 1
params = 'page={}&limit={}'.format(page_param, limit_param)
req = urllib.request.Request(url + params, headers={'User-Agent': 'Mozilla/5.0'})
response = urllib.request.urlopen(req)
data = json.loads(response.read())
# print(data)

# for i in range(0, data['data']['limit']):
#     movies = data['data']['movies'][i]
#     # print(movies)

movie_json = data['data']['movies'][0]
movie_info = MovieInfo.objects.create(movie_json)
