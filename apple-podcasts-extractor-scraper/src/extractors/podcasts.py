thonimport requests
from config.settings import Settings

def fetch_podcasts(query, limit):
    url = f"https://itunes.apple.com/search?term={query}&entity=podcast&limit={limit}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        raise Exception(f"Failed to fetch podcasts: {response.status_code}")