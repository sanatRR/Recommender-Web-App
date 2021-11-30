import http.client
import json


#returns URL of the poster, "-1" on errer
def get_poster(movie_name):
    conn = http.client.HTTPSConnection("imdb-internet-movie-database-unofficial.p.rapidapi.com")
    headers = {
    'x-rapidapi-host': "imdb-internet-movie-database-unofficial.p.rapidapi.com",
    'x-rapidapi-key': "0b9c3bb71cmsha990fbcbca0e8e6p1a5894jsnc0101b1bb302"
    }
    try:
        conn.request("GET", "/search/"+movie_name, headers=headers)
        res = conn.getresponse()
        data = res.read()
        data = data.decode("utf-8")
        info = json.loads(data)
        return info["titles"][0]["image"]
    except:
        return "-1"

