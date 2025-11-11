thonimport requests

class PodcastParser:
    def __init__(self):
        self.base_url = "https://itunes.apple.com/search?term="

    def parse(self, query, limit):
        url = f"{self.base_url}{query}&limit={limit}"
        response = requests.get(url)
        response.raise_for_status()
        return response.json()