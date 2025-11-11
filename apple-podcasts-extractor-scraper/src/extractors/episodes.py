thonimport requests

def fetch_episodes(podcast_id):
    url = f"https://itunes.apple.com/lookup?id={podcast_id}&entity=podcastEpisode"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data['results']
    else:
        raise Exception(f"Failed to fetch episodes: {response.status_code}")