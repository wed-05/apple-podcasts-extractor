thonimport json
import os
from extractors.podcast_parser import PodcastParser
from extractors.episode_parser import EpisodeParser
from outputs.data_exporter import DataExporter

def run_scraper(query, limit=10):
    podcast_data = PodcastParser().parse(query, limit)
    episode_data = EpisodeParser().parse(podcast_data)

    DataExporter().export(podcast_data, episode_data)

if __name__ == "__main__":
    query = "Ngobrol Sore Semaunya"
    run_scraper(query)