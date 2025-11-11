thonclass EpisodeParser:
    def __init__(self):
        pass

    def parse(self, podcast_data):
        episodes = []
        for podcast in podcast_data['results']:
            episode = {
                'episodeName': podcast['collectionName'],
                'releaseDate': podcast['releaseDate'],
                'description': podcast['description'],
                'episodeUrl': podcast['collectionViewUrl']
            }
            episodes.append(episode)
        return episodes